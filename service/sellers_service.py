from .general_service import GeneralService
from ..dao import sellers_dao


class SellerService(GeneralService):
    _dao = sellers_dao
