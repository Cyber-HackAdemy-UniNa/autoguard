from google.oauth2 import service_account
from googleapiclient import _auth
import json
from datetime import timedelta,datetime,timezone
import platform
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

SCOPES = os.getenv('SCOPES').split(',')
INGESTION_API = os.getenv('INGESTION_API') 
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
CUSTOMER_ID = os.getenv('CUSTOMER_ID')

# Create a credential using Google Developer Service Account Credential and Chronicle API
# Scope.
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build an HTTP client to make authorized OAuth requests.
http_client = _auth.authorized_http(credentials)

vehicle_ip = requests.get('https://ident.me').text

def generate_timestamp():
    current_utc_time = datetime.utcnow()

    timezone_offset = timedelta(hours=2)  

    current_time_with_offset = current_utc_time.replace(tzinfo=timezone.utc) + timezone_offset

    timestamp_str = current_time_with_offset.isoformat()

    return timestamp_str 

def ingest_logs(enrichment_fields):
    
    body = json.dumps({
    "customer_id": CUSTOMER_ID,
    "events": [{
        "metadata": {
            "eventTimestamp": f"{generate_timestamp()}",
            "eventType": enrichment_fields.get("eventType")
        },
        "additional": {
            "fields" : {
            "Entity": "VEHICLE",
            "vin": enrichment_fields.get("vin"),
            "vehicle_ip": vehicle_ip,
            }},
        "target": {
            "hostname": f"{platform.node()}"
        },
        "securityResult": [{
            "category":  enrichment_fields.get("categories"),
            "description": enrichment_fields.get("description"),
            "severity": enrichment_fields["severity"],
            "alert_state": enrichment_fields["alert_state"],
            "action": enrichment_fields["action"] 
        }]
    }]
})
               
    response = http_client.request(INGESTION_API, 
                       method="POST", 
                       body=body)

    print(body)
    print(response[0].get('status'))



def send_location_logs(enrichment_fields):
    
    body = json.dumps({
    "customer_id": CUSTOMER_ID,
    "events": [{
        "metadata": {
            "eventTimestamp": f"{generate_timestamp()}",
            "eventType": enrichment_fields.get("eventType")
        },
         "additional": {
            "fields" : {
            "Entity": "VEHICLE",
            "vin": enrichment_fields.get("vin"),
            "issuer_ip": enrichment_fields.get("issuer_ip"),
            "issuer_location": enrichment_fields.get("issuer_location"),
            "vehicle_ip": vehicle_ip,
            "vehicle_location": enrichment_fields.get("vehicle_location")
            }
        },
        "target": {
            "hostname": f"{platform.node()}"
        },
        "securityResult": [{
            "category": enrichment_fields["categories"],
            "description": enrichment_fields["description"],
            "severity": enrichment_fields["severity"],
            "alert_state": enrichment_fields["alert_state"],
            "action": enrichment_fields["action"] 
        }]
    }]
})
               
    response = http_client.request(INGESTION_API, 
                       method="POST", 
                       body=body)
    print(body)
    print(response[0].get('status'))


def ingest_location_log_if_mismatch(issuer_ip,vin):
    myip_address = get_ip()
    response = requests.get(f'http://ip-api.com/json/{myip_address}').json()
    mycountry = response.get("country")

    response = requests.get(f'http://ip-api.com/json/{issuer_ip}').json()
    issuer_country = response.get("country")

    if(mycountry!=issuer_country):

        enrichment_fields={
        "eventType": "USER_RESOURCE_ACCESS",
        "issuer_ip": issuer_ip,
        "issuer_location": issuer_country,
        "vehicle_location": mycountry,
        "vin": vin,
        "categories": ["ACL_VIOLATION"],
        "description": 'LOCATION_MISMATCH: An user issued a remote control command from a different location than the actual vehicle.',
        "severity": "HIGH",
        "alert_state": "ALERTING",
        "action":  "BLOCK"
        }

        send_location_logs(enrichment_fields)

    return mycountry==issuer_country


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]





       
