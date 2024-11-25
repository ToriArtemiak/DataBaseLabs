from .general_service import GeneralService
from ..dao import car_feature_values_dao


class CarFeatureValueService(GeneralService):
    _dao = car_feature_values_dao
