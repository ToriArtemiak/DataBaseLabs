from .general_service import GeneralService
from ..dao import car_features_dao


class CarFeatureService(GeneralService):
    _dao = car_features_dao
