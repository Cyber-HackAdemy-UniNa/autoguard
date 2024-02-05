from functools import wraps
from flask import request


def collect_request_info(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
    
        http_payload = None
        content_type = request.headers.get('Content-Type')
        if(request.method == 'POST'):
            if ('multipart/form-data' in content_type):
                http_payload = request.form
            elif ('application/json' in content_type):
                http_payload = request.get_json()
                
        http_info = {
            "ip" : request.remote_addr,
            "httpHeader": request.headers,
            "httpPayload": http_payload
        }
            
        request.http_info = http_info
        
        return func(*args, **kwargs)
    
    return decorated_function    


