from functools import wraps
from flask import Response, request
import json
import siem.siem_ingestor as siem_ingestor

def validate_content_type_multipart_form(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        content_type = request.headers.get('Content-Type')
        if ('multipart/form-data' not in content_type):
            msg = {'message': f'Content-Type {content_type} not supported'}
            siem_ingestor.ingest_invalid_content_type(content_type)
            
            return Response(json.dumps(msg), mimetype='application/json', status=400)
        return func(*args, **kwargs)

    return decorated_function

def validate_content_type_json(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        content_type = request.headers.get('Content-Type')
        if ('application/json' not in content_type):
            msg = {'message': f'Content-Type {content_type} not supported'}
            siem_ingestor.ingest_invalid_content_type(content_type)
            
            return Response(json.dumps(msg), mimetype='application/json', status=400)

        return func(*args, **kwargs)

    return decorated_function

def validate_opened(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        body = request.get_json()

        if 'opened' not in body or body['opened'] is None or body['opened'].lower() not in ['true', 'false']:
            msg = {'message': 'Bad Request: invalid "opened" parameter specified.'}
            siem_ingestor.ingest_invalid_opened_parameter({body['opened'] if 'opened' in body else "None"})
            
            return Response(response=json.dumps(msg), mimetype='application/json', status=400)

        return func(*args, **kwargs)

    return decorated_function

def validate_side(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        body = request.get_json()
        if 'side' not in body or body['side'] is None or body['side'].lower() not in ['left', 'right']:
            msg = {'message': 'Bad Request: invalid "side" parameter specified.'}
            siem_ingestor.ingest_invalid_side_parameter({body['side'] if 'side' in body else "None"})

            return Response(json.dumps(msg), mimetype='application/json', status=400)

        return func(*args, **kwargs)

    return decorated_function

def validate_vin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        vin = ''
        content_type = request.headers.get('Content-Type')
        if ('multipart/form-data' in content_type):
            vin = request.form.get('vin')
        elif ('application/json' in content_type):
            vin = request.get_json()['vin']

        if vin is None:
            msg = {'message': 'Bad Request, vin cannot be none'}
            siem_ingestor.ingest_invalid_vin_parameter(vin)
            
            return Response(json.dumps(msg), mimetype='application/json', status=400)
        return func(*args, **kwargs)
    return decorated_function

def validate_association_token(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        files = request.files
        try:
            if 'token' not in request.files or files['token'] is None:
                msg={'message': 'Association token not provided.'}
                return Response(json.dumps(msg), mimetype='application/json', status=400)
            
            request.association_token = files['token'].read().decode('utf-8')
        except:
            msg={'message': 'Token corrupted, please assure to provide txt file'}
            siem_ingestor.ingest_corrupted_association_token()
            
            return Response(json.dumps(msg), mimetype='application/json', status=400)

        return func(*args, **kwargs)
    return decorated_function

def validate_image(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        files = request.files
        if 'image' not in files or files['image'] is None:
             msg={'message': 'Bad Request, image not uploaded'} 
             return Response(json.dumps(msg), mimetype='application/json', status=400)        
        try:
            request.image = {
                    "data": files['image'].read(),
                    "filename": files['image'].filename
                }
        except:
            msg={'message': 'Bad Request, image corrupted'}
            siem_ingestor.ingest_invalid_image()

            return Response(json.dumps(msg), mimetype='application/json', status=400)
        
        return func(*args, **kwargs)
    return decorated_function



