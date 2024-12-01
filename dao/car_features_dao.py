# car_features_dao.py
from app.domain import CarFeature
from app.dao.general_dao import GeneralDAO

class CarFeatureDAO(GeneralDAO):
    _domain_type = CarFeature
