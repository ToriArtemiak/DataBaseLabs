# car_feature_values_dao.py
from app.domain import CarFeatureValue
from app.dao.general_dao import GeneralDAO

class CarFeatureValueDAO(GeneralDAO):
    _domain_type = CarFeatureValue
