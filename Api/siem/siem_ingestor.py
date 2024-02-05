from flask import request
from siem.siem import ingest_logs

def ingest_IDOR_vehicle_control(vehicle_id):

    ingest_logs(http_info=request.http_info, enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 401,
        "uid":  request.token["uid"],
        "categories": ["ACL_VIOLATION"],
        "description": f'IDOR detected!: User do not own this vehicle {vehicle_id}',
        "severity": "HIGH",
        "alert_state": "ALERTING",
        "action":  "BLOCK"
    })    

def ingest_invalid_auth_token(exception):
    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "statusCode": 401,
            "uid": "None",
            "categories": ["AUTH_VIOLATION"],
            "description": exception,
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })   

def ingest_vehicle_already_associated():
    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "USER_RESOURCE_ACCESS",
            "statusCode": 500,
            "uid":  request.token["uid"],
            "categories": ["ACL_VIOLATION"],
            "description": "Vehicle already associated.",
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })    

def ingest_invalid_content_type(content_type):

    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "NETWORK_HTTP",
            "statusCode": 400,
            "uid": request.token["uid"],
            "categories": ["SOFTWARE_SUSPICIOUS"],
            "description": f'Content-Type {content_type} not supported',
            "severity": "LOW",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })

def ingest_invalid_opened_parameter(opened):

    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "NETWORK_HTTP",
            "statusCode": 400,
            "uid": request.token["uid"],
            "categories": ["SOFTWARE_SUSPICIOUS"],
            "description": f'Bad Request: invalid "opened" parameter specified: {opened}',
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })

def ingest_invalid_side_parameter(side):
    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "NETWORK_HTTP",
            "statusCode": 400,
            "uid": request.token["uid"],
            "categories": ["SOFTWARE_SUSPICIOUS"],
            "description": f'Bad Request: invalid "side" parameter specified: {side}',
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })

def ingest_invalid_vin_parameter(vin):
    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "NETWORK_HTTP",
            "statusCode": 400,
            "uid": request.token["uid"],
            "categories": ["SOFTWARE_SUSPICIOUS"],
            "description": f'Bad Request: invalid "vin" parameter specified: {vin}',
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })

def ingest_corrupted_association_token():
    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "NETWORK_HTTP",
            "statusCode": 400,
            "uid": request.token["uid"],
            "categories": ["SOFTWARE_SUSPICIOUS"],
            "description": 'Bad Request: corrupted association token.',
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })

def ingest_invalid_image():
    ingest_logs(http_info=request.http_info, enrichment_fields={
            "eventType": "NETWORK_HTTP",
            "statusCode": 400,
            "uid": request.token["uid"],
            "categories": ["SOFTWARE_SUSPICIOUS"],
            "description": 'Bad Request: corrupted image.',
            "severity": "MEDIUM",
            "alert_state": "ALERTING",
            "action":  "BLOCK"
        })
   
def ingest_association_init_failed():
    
    ingest_logs(http_info=request.http_info,enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 500,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Something went wrong: Invalid hashed token or button not pressed in time.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "BLOCK"
        })

def ingest_association_successful():
    ingest_logs(http_info=request.http_info,enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 200,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Vehicle successfully associated to user.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "ALLOW"
        })

def ingest_association_failed():
    ingest_logs(http_info=request.http_info,enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 500,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Could not associate vehicle to user.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "FAIL"
        })
    
def ingest_door_command_successful():
    ingest_logs(http_info=request.http_info,enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 200,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Door command sent successfully.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "ALLOW"
        })

def ingest_door_command_failed():
    ingest_logs(http_info=request.http_info, enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 500,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Could not send door command.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "FAIL"
        })

def ingest_get_user_vehicles_successful():
    ingest_logs(http_info=request.http_info, enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 200,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "User requested and successfully got a list of its vehicles.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "ALLOW"
        })

def ingest_get_user_vehicles_failed():
    ingest_logs(http_info=request.http_info, enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 500,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "User requested but could not get a list of its vehicles.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "FAIL"
        })


def ingest_headlights_command_successful():
    ingest_logs(http_info=request.http_info, enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 200,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Headlight command sent successfully.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "ALLOW"
        })

def ingest_headlights_command_failed():
    ingest_logs(http_info=request.http_info, enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "statusCode": 500,
        "uid": request.token["uid"],
        "categories": ["UNKNOWN_CATEGORY"],
        "description": "Could not send headlight command.",
        "severity": "NONE",
        "alert_state": "NOT_ALERTING",
        "action": "FAIL"
        })