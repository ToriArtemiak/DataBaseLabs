# cars_dao.py
from app.domain import Car
from app.dao.general_dao import GeneralDAO

class CarDAO(GeneralDAO):
    _domain_type = Car

    def find_by_seller_id(self, seller_id: int):
        return self._domain_type.query.filter_by(seller_id=seller_id).all()
