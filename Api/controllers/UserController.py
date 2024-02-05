from models import Vehicle
from database.firebase import FieldFilter, USERS_COLLECTION_NAME, IMAGES_BUCKET_NAME, VEHICLES_COLLECTION_NAME, vehicle_images_bucket
import uuid
from exceptions.UserNotExistsException import UserNotExistsException
from exceptions.GenericDatabaseException import GenericDatabaseException

class UserController:

    def __init__(self, firestore, cloud_storage):
        self._firestore = firestore
        self._cloud_storage = cloud_storage  

    def save_association(self, vehicle: Vehicle, image: dict):

        try:
            
            image_link = self._save_image(image)

            vehicle.set_image_link(image_link)

            update_time, vehicle_ref = self._firestore.collection(VEHICLES_COLLECTION_NAME).add(vehicle.to_dict()) # First save vehicle to vehicles collection..
            
            users_collection = self._firestore.collection(USERS_COLLECTION_NAME)
            
            uid = vehicle.get_user_id()
            user_query = users_collection.where(filter=FieldFilter("uid", "==", uid)) # Get user by given uid 
           
            user_refs_list = list(user_query.stream())
                                    
            if not user_refs_list: #User does not exist on DB
                raise UserNotExistsException(f'User with uid {uid} not found')
            
            old_vehicles = []
                        
            user_dict = user_refs_list[0].to_dict()
            
            if 'vehicles' in user_dict:
                old_vehicles = user_dict['vehicles']
            
            old_vehicles.append(vehicle_ref) # Add the new vehicle to user's vehicles

            new_vehicles = old_vehicles

            users_collection.document(uid).update({"vehicles": new_vehicles}) # Update user's vehicles
                                
        except Exception as e:
            raise GenericDatabaseException(f'Something went wrong: {e}')
    
    def get_user_vehicles(self, uid: str) -> list[dict]:
        
        users_collection = self._firestore.collection(USERS_COLLECTION_NAME)
        user_query = users_collection.where(filter=FieldFilter("uid", "==", uid))
        
        user_refs_list = list(user_query.stream())
                        
        if not user_refs_list: #User does not exist on DB
            raise UserNotExistsException(f'User with uid {uid} not found')

        user_dict = user_refs_list[0].to_dict() 

        if 'vehicles' not in user_dict:
            user_dict['vehicles'] = []

        vehicle_references = user_dict['vehicles']

        vehicles_dict = []

        for vehicle_reference in vehicle_references:
            vehicle_dict = vehicle_reference.get().to_dict()
            vehicle_dict['id'] = vehicle_reference.id
            vehicles_dict.append(vehicle_dict)
        return vehicles_dict
    
    def get_vehicle_vin(self, id: str) -> dict:
        
        try:
            vehicles_collection = self._firestore.collection(VEHICLES_COLLECTION_NAME)
            vehicle_doc = vehicles_collection.document(id)     
            
            vehicle_snapshot = vehicle_doc.get()

            return vehicle_snapshot.to_dict()['vin'] if vehicle_snapshot.exists else None
        except Exception as e:
            raise GenericDatabaseException(f'Something went wrong: {e}')
    

    def _save_image(self, image: dict) -> str: 

        try:
            download_token = str(uuid.uuid4())
            filename = image['filename']
            data = image['data']
            
            blob = vehicle_images_bucket.blob(filename)
            blob.metadata = { "cacheControl": "max-age=31536000",
                "firebaseStorageDownloadTokens": download_token,
            }
            blob.upload_from_string(data)

            image_link = self._get_firebase_storage_file_link(bucket_name=IMAGES_BUCKET_NAME, 
                                                        file_name=filename, 
                                                        download_token=download_token)
            return image_link
        except Exception as e:
            raise GenericDatabaseException(f'Something went wrong: {e}')


    def _get_firebase_storage_file_link(self, bucket_name: str, file_name: str, download_token: str):
        return f"https://firebasestorage.googleapis.com/v0/b/{bucket_name}/o/{file_name}?alt=media&token={download_token}"


