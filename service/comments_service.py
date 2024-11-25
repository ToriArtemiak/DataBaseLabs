from .general_service import GeneralService
from ..dao import comments_dao


class CommentService(GeneralService):
    _dao = comments_dao
