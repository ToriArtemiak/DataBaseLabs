# sellers_dao.py
from app.domain import Seller
from app.dao.general_dao import GeneralDAO

class SellerDAO(GeneralDAO):
    _domain_type = Seller
