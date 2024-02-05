class Vehicle:
    
    def __init__(self, vin=None, plate_number=None, model=None, image_link=None, id=None, uid=None):
        self._vin = vin
        self._plate_number = plate_number
        self._model = model
        self._image_link = image_link
        self._uid = uid
        self._id = id
    
    @staticmethod
    def from_dict(source):
        vehicle = Vehicle(
            vin=source.get('vin'),
            id=source['id'],
            plate_number=source['plateNumber'],
            model=source['model'],
            image_link=source['imageLink'],
            uid=source['uid']
        )
        return vehicle

    def to_dict(self):
        return {
            'vin': self._vin,
            'plateNumber': self._plate_number,
            'model': self._model,
            'imageLink': self._image_link,
            'uid': self._uid
        }

    def get_plate_number(self):
        return self._plate_number

    def get_model(self):
        return self._model

    def get_id(self):
        return self._id

    def get_image_link(self):
        return self._image_link

    def get_user_id(self):
        return self._uid
    
    def get_vin(self):
        return self._vin

    def set_image_link(self, image_link: str):
        self._image_link = image_link

    def __str__(self):
        return f"Vehicle(id={self._id}, vin={self._vin}, plate_number={self._plate_number}, model={self._model}, image_link={self._image_link}, uid={self._uid})"
