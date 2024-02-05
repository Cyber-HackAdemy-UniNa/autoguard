import json
from mqtt.mqtt import simple_subscribe

class MqttVehicleController:

    def __init__(self, mqtt_client):
        self._mqtt_client = mqtt_client    
    
    def request_association(self, vin: str,token: str, issuer_ip: str) -> dict:
        topic=f"/vehicles/{vin}/pair"
        msg = {'token': token, 'issuer_ip': issuer_ip}
        resultpub = self._mqtt_client.publish(topic, json.dumps(msg)) 
        status = resultpub[0]
    
        if status == 0:
            topicsub=f"/vehicles/{vin}$/pair-response"
            
            resultsub= simple_subscribe(topicsub,1)
            return json.loads(resultsub.payload.decode())
        
        result={'message': "Failed to request association",'status': 'error'}
        return result

        
    def set_doors(self, vin: str, side: str, opened: bool, issuer_ip: str) -> str:
        topic=f"/vehicles/{vin}/doors"
        msg = {'side': side, 'opened': opened, 'issuer_ip': issuer_ip}
        resultpub = self._mqtt_client.publish(topic, json.dumps(msg))
        status = resultpub[0]
        return status
    
    def set_headlights(self, vin: str, opened: bool, issuer_ip: str) -> str:
        topic=f"/vehicles/{vin}/headlights"
        msg = {'opened': opened, 'issuer_ip': issuer_ip}
        resultpub = self._mqtt_client.publish(topic, json.dumps(msg)) 
        status = resultpub[0]
        return status
