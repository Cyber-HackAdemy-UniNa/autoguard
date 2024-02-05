import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from google.cloud.firestore_v1.base_query import FieldFilter
from google.cloud import storage

VEHICLES_COLLECTION_NAME = 'vehicles'

USERS_COLLECTION_NAME = 'users'

IMAGES_BUCKET_NAME = 'autoguard-vehicles-images'

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

cloud_storage = storage.Client()

vehicle_images_bucket = cloud_storage.bucket(IMAGES_BUCKET_NAME)


