# car_photos_dao.py
from app.domain import CarPhoto
from app.dao.general_dao import GeneralDAO

class CarPhotoDAO(GeneralDAO):
    _domain_type = CarPhoto
