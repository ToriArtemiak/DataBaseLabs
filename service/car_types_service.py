from .general_service import GeneralService
from ..dao import car_types_dao


class CarTypeService(GeneralService):
    _dao = car_types_dao
