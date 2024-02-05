from flask import Flask, request
from controllers.MqttVehicleController import MqttVehicleController
from controllers.UserController import UserController
from mqtt.mqtt import connect as mqtt_connect
from database.firebase import firestore_client, cloud_storage
from middlewares.auth_middleware import *
from middlewares.validate_middleware import *
import siem.siem_ingestor as siem_ingestor
from middlewares.siem_middleware import *
from middlewares.vehicle_middleware import *
from models.Vehicle import Vehicle 

app = Flask(__name__)

mqtt_client = mqtt_connect()
mqtt_vehicle_controller = MqttVehicleController(mqtt_client)
user_controller = UserController(firestore_client, cloud_storage)

@app.route("/vehicles", methods = ['GET'])
@collect_request_info
@validate_firebase_token
@validate_content_type_json
def get_user_vehicles():
    
    uid = request.token['uid']

    try:
        vehicles=user_controller.get_user_vehicles(uid)
        response= Response(response=json.dumps({"vehicles": vehicles, "vehicles_number": len(vehicles)}), mimetype='application/json', status=200)
        siem_ingestor.ingest_get_user_vehicles_successful()
    except:
        response= Response(response=json.dumps({'message': 'Something went wrong.'}), mimetype='application/json', status=500)
        siem_ingestor.ingest_get_user_vehicles_failed()

    return response

@app.route("/vehicles/rpc/doors", methods = ['POST'])
@collect_request_info
@validate_firebase_token
@validate_content_type_json
@validate_opened
@validate_side
@validate_vehicle_ownership
def set_doors():
    body = request.get_json()

    vin = user_controller.get_vehicle_vin(body['id'])
    opened=body['opened']
    side=body['side']
    issuer_ip = request.remote_addr
    status=mqtt_vehicle_controller.set_doors(vin, side, opened, issuer_ip)
        
    if status==0:
        response=Response(response=json.dumps({"message": "Door command sent successfully."}), mimetype='application/json', status=200)
        siem_ingestor.ingest_door_command_successful()
    else: 
        response=Response(response=json.dumps({"message": "Could not send door command."}), mimetype='application/json', status=500)
        siem_ingestor.ingest_door_command_failed()

    return response


@app.route("/vehicles/rpc/headlights", methods = ['POST'])
@collect_request_info
@validate_firebase_token
@validate_vehicle_ownership
@validate_content_type_json
@validate_opened
def set_headlights():
    
    body = request.get_json()

    vin = user_controller.get_vehicle_vin(body['id'])
    opened=body['opened']
    issuer_ip = request.remote_addr
    status=mqtt_vehicle_controller.set_headlights(vin, opened, issuer_ip)
        
    response=None
    if status==0:
        response=Response(response=json.dumps({"message": "Headlight command sent successfully."}), mimetype='application/json', status=200)
        siem_ingestor.ingest_headlights_command_successful()
    else:
        response=Response(response=json.dumps({"message": "Could not send headlight command."}), mimetype='application/json', status=500)
        siem_ingestor.ingest_headlights_command_failed()
        
    return response

@app.route("/associate", methods = ['POST'])
@collect_request_info
@validate_firebase_token
@validate_content_type_multipart_form
@validate_vin
@validate_association_token
@validate_image
@validate_vehicle_association
def save_association():
    form_data = request.form
    
    association_token = request.association_token

    vin=form_data.get('vin')
    issuer_ip = request.remote_addr
    result=mqtt_vehicle_controller.request_association(vin, association_token, issuer_ip)
    status = result.get('status')

    if "error" in status:
        response=Response(response=json.dumps(result), mimetype='application/json', status=500)  #possible errors: association_token expected,invalid hashed token, button not pressed
        siem_ingestor.ingest_association_init_failed()
    else:
        plate_number=form_data.get('plateNumber')
        model=form_data.get('model')
            
        uid = request.token['uid']
        image=request.image

        vehicle = Vehicle(vin=vin, plate_number=plate_number, model=model, uid=uid)
            
        try:
            user_controller.save_association(vehicle=vehicle, image=image)
            response=Response(response=json.dumps({'message': 'Vehicle succesfully associated.'}), mimetype='application/json', status=200)
            siem_ingestor.ingest_association_successful()
        except:
            response=Response(response=json.dumps({'message': 'Could not associate vehicle.'}), mimetype='application/json', status=500)
            siem_ingestor.ingest_association_failed()

    return response

if __name__ == "__main__":
    mqtt_client.loop_start()
    # ssl_context = ('./ssl/fullchain.pem', './ssl/privkey.pem')   
    # app.run(host='0.0.0.0', port=2053, ssl_context=ssl_context) 


  

   
   

    
    
    
