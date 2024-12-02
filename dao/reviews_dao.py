from app.domain import Review
from app.dao.general_dao import GeneralDAO


class ReviewDAO(GeneralDAO):
    _domain_type = Review