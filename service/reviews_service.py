from .general_service import GeneralService
from ..dao import reviews_dao


class ReviewService(GeneralService):
    _dao = reviews_dao
