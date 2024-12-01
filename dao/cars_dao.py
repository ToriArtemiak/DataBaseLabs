# cars_dao.py
from app.domain import Car
from app.dao.general_dao import GeneralDAO

class CarDAO(GeneralDAO):
    _domain_type = Car
