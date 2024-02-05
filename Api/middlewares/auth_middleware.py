from functools import wraps
from flask import Response, request
from database.firebase import auth
import json
from siem.siem_ingestor import ingest_invalid_auth_token

def validate_firebase_token(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        authorization=request.headers.get('Authorization')
        try:
            token = authorization.split()[1]
            decoded_token = auth.verify_id_token(token)
            request.token = decoded_token ## Pass token to next middlewares
            return func(*args, **kwargs)
        except Exception as e:
            ingest_invalid_auth_token(e)
            return Response(json.dumps({'message': 'Token not valid'}), mimetype='application/json', status=401)

    return decorated_function
