import requests

def check_location_mismatch(issuer_ip) -> dict:
    vehicle_ip = requests.get('https://ident.me').text
    
    response = requests.get(f'http://ip-api.com/json/{vehicle_ip}').json()
    vehicle_location = response.get("country")
    
    response = requests.get(f'http://ip-api.com/json/{issuer_ip}').json()
    issuer_location = response.get("country")
    
    if(issuer_location != vehicle_location):
        return {'result' : True,
                'vehicle_location': vehicle_location,
                'issuer_location': issuer_location,
                'issuer_ip': issuer_ip,
                'vehicle_ip': vehicle_ip}
    return {'result': False}