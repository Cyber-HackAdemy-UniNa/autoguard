from paho.mqtt import client as mqtt_client
import paho.mqtt.subscribe as subscribe
from dotenv import load_dotenv
import os

env_file_path = 'mqtt/.env'
load_dotenv(dotenv_path=env_file_path)

BROKER = os.getenv('BROKER')
PORT = int(os.getenv('PORT'))
PASSWORD = os.getenv('PASSWORD')
USERNAME = os.getenv('USERNAME')
CLIENT_ID = os.getenv('CLIENT_ID')

def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f'🚀Connected to MQTT emqx Broker [{BROKER}:{PORT}]🚀')
        else:
            print("Failed to connect, return code %d\n" % rc)   
                
    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(
        ca_certs='./.truststore/ca.pem',
        certfile='./.keystore/client.pem',
        keyfile='./.keystore/client.key'
    )
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def simple_subscribe(topic: str, msg_count: int) -> (list[mqtt_client.MQTTMessage]):
    return subscribe.simple(topic,
                            msg_count=msg_count,
                            hostname=BROKER,port=PORT,
                            client_id="Server2",
                            auth={'username':USERNAME,'password':PASSWORD},
                            tls={'ca_certs': './.truststore/ca.pem',
                            'certfile': './.keystore/client.pem',
                            'keyfile': './.keystore/client.key'})
    

    
