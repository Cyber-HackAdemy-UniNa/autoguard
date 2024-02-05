from functools import wraps
from flask import Response, request
from database.firebase import firestore_client, FieldFilter, VEHICLES_COLLECTION_NAME, USERS_COLLECTION_NAME
from exceptions.UserNotExistsException import UserNotExistsException
import json
from siem.siem_ingestor import ingest_vehicle_already_associated, ingest_IDOR_vehicle_control

def validate_vehicle_association(func): # Requested vehicle must not be already associated
    @wraps(func)
    def decorated_function(*args, **kwargs):
        vin = ''
        content_type = request.headers.get('Content-Type')
        if ('multipart/form-data' in content_type):
            vin = request.form.get('vin')
        elif ('application/json' in content_type):
            vin = request.get_json()['vin']
        
        vehicles_collection = firestore_client.collection(VEHICLES_COLLECTION_NAME)
        vehicles_query = vehicles_collection.where(filter=FieldFilter("vin", "==", vin))

        vehicles_ref_list = list(vehicles_query.stream())

        if vehicles_ref_list: # If there is already a vehicle with this vin, that vehicle is already associated so request fails
            ingest_vehicle_already_associated()
            return Response(json.dumps({'message': 'Vehicle already associated'}), mimetype='application/json', status=500)
        return func(*args, **kwargs)
    return decorated_function
 
def validate_vehicle_ownership(func): # User can only control vehicles he owns
    @wraps(func)
    def decorated_function(*args, **kwargs):
        request_vehicle_id = request.get_json()['id']
        uid = request.token['uid']
            
        users_collection = firestore_client.collection(USERS_COLLECTION_NAME)
        user_query = users_collection.where(filter=FieldFilter("uid", "==", uid)) # Get user by given uid 
        
        user_refs_list = list(user_query.stream())
                     
        if not user_refs_list: #User does not exist on DB
            raise UserNotExistsException(f'User with uid {uid} not found')
        
        user_dict = user_refs_list[0].to_dict()

        vehicle_references = user_dict['vehicles']

        for vehicle_reference in vehicle_references: # Iterates over all user vehicles and checks if request_vehicle_id matches with a user's vehicle id
            if vehicle_reference.id.strip() == request_vehicle_id:
                return func(*args, **kwargs) 
            
        ingest_IDOR_vehicle_control(request_vehicle_id)
        return Response(json.dumps({'message': 'Vehicle requested does not belong to current user.'}), mimetype='application/json', status=401)      

    return decorated_function
