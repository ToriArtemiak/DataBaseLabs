from .general_service import GeneralService
from ..dao import car_photos_dao


class CarPhotoService(GeneralService):
    _dao = car_photos_dao
