from .general_service import GeneralService
from ..dao import dealership_dao


class DealershipService(GeneralService):
    _dao = dealership_dao
