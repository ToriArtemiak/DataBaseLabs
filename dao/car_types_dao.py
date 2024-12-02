# car_types_dao.py
from app.domain import CarType
from app.dao.general_dao import GeneralDAO

class CarTypeDAO(GeneralDAO):
    _domain_type = CarType
