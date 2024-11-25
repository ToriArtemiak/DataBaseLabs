# dealerships_dao.py
from app.domain import Dealership
from app.dao.general_dao import GeneralDAO


class DealershipDAO(GeneralDAO):
    _domain_type = Dealership
