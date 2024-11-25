from .general_service import GeneralService
from ..dao import cars_dao


class CarService(GeneralService):
    _dao = cars_dao
