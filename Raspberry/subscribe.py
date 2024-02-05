from paho.mqtt import client as mqtt_client
from dotenv import load_dotenv
from paho.mqtt import publish
from util import check_token, print_token
from vehicle_controller import is_button_pressed_within_timeout, control_door, control_headlights
import siem_ingestor
import os
import json
from siem import ingest_location_log_if_mismatch

print_token()
env_file_path = '.env'
load_dotenv(env_file_path)

BROKER = os.getenv('BROKER')
PORT = int(os.getenv('PORT'))
PASSWORD = os.getenv('PASSWORD')
USERNAME = os.getenv('USERNAME')
CLIENT_ID = vin = os.getenv('VIN')

PAIR_RPC_TOPIC = f'/vehicles/{vin}/pair'
DOORS_RPC_TOPIC = f'/vehicles/{vin}/doors'
HEADLIGHTS_RPC_TOPIC = f'/vehicles/{vin}/headlights'

client_id_request_pair = CLIENT_ID + "$"

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f'🚀Connected to MQTT emqx Broker [{BROKER}:{PORT}]🚀')
            siem_ingestor.ingest_broker_connection_successful(vin, BROKER, PORT)
        else:
            siem_ingestor.ingest_broker_connection_failed(vin, BROKER, PORT)

    client = mqtt_client.Client(vin)
    client.tls_set(
        ca_certs='./.truststore/ca.pem',
        certfile='./.keystore/client.pem',
        keyfile='./.keystore/client.key'
    ) 
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client

def publish_single(topic: str, payload: str):
    publish.single(
        topic=topic,
        payload=payload,
        hostname=BROKER,
        port=PORT,
        client_id=client_id_request_pair,
        auth={'username': USERNAME, 'password': PASSWORD},
        tls={'ca_certs': './.truststore/ca.pem',
             'certfile': './.keystore/client.pem',
             'keyfile': './.keystore/client.key'}
    )
    
def subscribe_doors(client: mqtt_client, topic: str):
        
    def on_message(client, userdata, msg):
        json_msg = json.loads(msg.payload.decode())
        opened = json.loads(msg.payload.decode())['opened'].lower()
        if ingest_location_log_if_mismatch(json_msg['issuer_ip'],vin) is True:
            if control_door(json_msg['side'], opened) is True:
                siem_ingestor.ingest_door_command_successful(vin, topic, json_msg['side'],opened)
            else:
                siem_ingestor.ingest_door_command_failed(vin, topic, json_msg['side'],opened)
        
    client.subscribe(topic)
    client.message_callback_add(topic, on_message)

def subscribe_headlights(client: mqtt_client,topic:str):

    def on_message(client, userdata, msg):
        json_msg = json.loads(msg.payload.decode())

        opened = json.loads(msg.payload.decode())['opened'].lower()
        if ingest_location_log_if_mismatch(json_msg['issuer_ip'],vin) is True:
            if control_headlights(opened) is True:
                siem_ingestor.ingest_headlights_command_successful(vin, topic,opened)
            else:
                siem_ingestor.ingest_headlights_command_failed(vin, topic,opened)  
          
    client.subscribe(topic)
    client.message_callback_add(topic, on_message)

def subscribe_pair(client: mqtt_client, topic: str):

    def on_message(client, userdata, msg):

        topic=f"/vehicles/{vin}$/pair-response"
        json_msg=json.loads(msg.payload.decode())

        if ingest_location_log_if_mismatch(json_msg['issuer_ip'],vin) is False:
            return
        token=json_msg.get('token')
        
        if token is None:
            msg = {'message': 'token expected','status': 'error'}
            publish_single(topic,payload=json.dumps(msg))
            return
        pressed_within_timeout = is_button_pressed_within_timeout(timeout = 3)
       
        if pressed_within_timeout is False:
            msg = {'message': 'Button not pressed in time','status': 'error'}
            siem_ingestor.ingest_button_not_pressed_in_time(vin, topic)  
            publish_single(topic=topic,payload=json.dumps(msg))        
            return    
        
        is_token_valid = check_token(token)

        if is_token_valid:
            msg = {'message': 'Token accepted','status': 'success'}
            siem_ingestor.ingest_association_token_valid(vin, topic)
        else:
            msg = {'message': 'Invalid token','status': 'error'}
            siem_ingestor.ingest_association_token_invalid(vin, topic)   
        publish_single(topic,payload=json.dumps(msg))
    client.subscribe(topic)
    client.message_callback_add(topic, on_message)

def run():
    client = connect_mqtt()
    subscribe_doors(client, DOORS_RPC_TOPIC)
    subscribe_pair(client, PAIR_RPC_TOPIC)
    subscribe_headlights(client, HEADLIGHTS_RPC_TOPIC)
    client.loop_forever()

if __name__ == '__main__':
    run()
