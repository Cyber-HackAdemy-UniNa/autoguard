from siem.siem import ingest_logs, ingest_location_logs

def ingest_location_mismatch(vin, location_mismatch):
    ingest_location_logs(enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "issuer_ip": location_mismatch['issuer_ip'],
        "issuer_location": location_mismatch['issuer_location'],
        "vehicle_location": location_mismatch['vehicle_location'],
        "vehicle_ip": location_mismatch['vehicle_ip'],
        "issuer_latitude": location_mismatch['issuer_latitude'],
        "issuer_longitude": location_mismatch['issuer_longitude'],
        "vin": vin,
        "categories": ["ACL_VIOLATION"],
        "description": 'LOCATION_MISMATCH: An user issued a remote control command from a different location than the actual vehicle.',
        "severity": "HIGH",
        "alert_state": "ALERTING",
        "action":  "BLOCK"
        })    
    
def ingest_broker_connection_successful(vin, broker, port):
    ingest_logs(enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "vin": vin,
        "categories": ["UNKNOWN_CATEGORY"],
        "description": f"Vehicle connected to MQTT EMQX Broker mqtts://{broker}:{port}",
        "severity": "LOW",
        "alert_state": "NOT_ALERTING",
        "action":  "ALLOW"
        })
    

def ingest_broker_connection_failed(vin, broker, port):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Vehicle could not connect to MQTT EMQX Broker [{broker}:{port}]',
            "severity": "LOW",
            "alert_state": "NOT_ALERTING",
            "action":  "FAIL"
            })

def ingest_door_command_successful(vin, topic, door_side,opened):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Successfully {"opened" if opened=="true" else "closed"} {door_side} door.',
            "alert_state": "NOT_ALERTING",
            "severity": "NONE",
            "action":  "ALLOW"
            })


def ingest_door_command_failed(vin, topic, door_side,opened):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Could not {"open" if opened=="true" else "close"} {door_side} door.',
            "alert_state": "NOT_ALERTING",
            "severity": "NONE",
            "action":  "FAIL"
            })


def ingest_headlights_command_successful(vin, topic,opened):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Successfully turned {"on" if opened=="true" else "off"} headlights.',
            "alert_state": "NOT_ALERTING",
            "severity": "NONE",
            "action":  "ALLOW"
            })

def ingest_headlights_command_failed(vin, topic,opened):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Could not turn {"open" if opened=="true" else "close"} headlights.',
            "alert_state": "NOT_ALERTING",
            "severity": "NONE",
            "action":  "FAIL"
            })

def ingest_button_not_pressed_in_time(vin, topic):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Error associating vehicle: button not pressed in time',
            "severity": "NONE",
            "alert_state": "NOT_ALERTING",
            "action":  "FAIL"
            }) 

def ingest_association_token_valid(vin, topic):
    ingest_logs(enrichment_issuer_latitudefields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Successfully validated association token.',
            "severity": "NONE",
            "alert_state": "NOT_ALERTING",
            "action":  "ALLOW"
            })

def ingest_association_token_invalid(vin, topic):
    ingest_logs(enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "vin": f"{vin}",
            "mqtt_topic": f"{topic}",
            "categories": ["UNKNOWN_CATEGORY"],
            "description": f'Error associating vehicle: association token is not valid',
            "severity": "NONE",
            "alert_state": "NOT_ALERTING",
            "action":  "FAIL"
            })