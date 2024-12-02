# comments_dao.py
from app.domain import Comment
from app.dao.general_dao import GeneralDAO


class CommentDAO(GeneralDAO):
    _domain_type = Comment
