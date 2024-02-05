class User:
    
    def __init__(self, id=None, email=None, vehicles=None):
        self._id = id
        self._email = email
        self._vehicles = vehicles

    @staticmethod
    def from_dict(source):
        user = User(
            id=source['uid'],
            email=source['email'],
            vehicles=source['vehicles'],
        )
        return user

    def to_dict(self):
        return {
            'uid': self._id,
            'email': self._email,
            'vehicles': self._vehicles,
        }

    def get_id(self):
        return self._id

    def get_email(self):
        return self._email

    def get_vehicles(self):
        return self._vehicles
    
    def set_image_link(self, image_link):
        self._image_link = image_link

    def __str__(self):
        return f"User(id={self._id}, email={self._email}, vehicles={self._vehicles})"
