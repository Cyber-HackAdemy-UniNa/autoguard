from google.oauth2 import service_account
from googleapiclient import _auth
import json
from datetime import timedelta,datetime,timezone
import platform


# SCOPES = ['https://www.googleapis.com/auth/malachite-ingestion']
# INGESTION_API = "https://europe-malachiteingestion-pa.googleapis.com/v2/udmevents:batchCreate"

# SERVICE_ACCOUNT_FILE = 'siem/chronicle_creds.json'

# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# http_client = _auth.authorized_http(credentials)


def generate_timestamp():
    current_utc_time = datetime.utcnow()

    timezone_offset = timedelta(hours=2)  

    current_time_with_offset = current_utc_time.replace(tzinfo=timezone.utc) + timezone_offset

    timestamp_str = current_time_with_offset.isoformat()

    return timestamp_str 

  
def ingest_logs(http_info,enrichment_fields):
        
        body = json.dumps({
            "customer_id": "81180cff-3e4c-4a92-a479-7798bdabfc67",
            "events": [{
                "metadata": {
                    "eventTimestamp": f"{generate_timestamp()}",
                    "eventType": enrichment_fields["eventType"]
                },
                "additional": {
                    "fields" : {
                        
                    "Entity": "CLOUD API",
                    "ip" : http_info.get("ip"),
                    "httpHeader" : f"{http_info.get('httpHeader') }",
                    "httpPayload" : f"{http_info.get('httpPayload')}",
                    "responseStatusCode": f"{enrichment_fields.get('statusCode')}",
                    "uid": enrichment_fields.get("uid")
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
        
        
        # response = http_client.request(INGESTION_API, 
        #                method="POST", 
        #                body=body)
        # print(response[0].get('status'))
        




       