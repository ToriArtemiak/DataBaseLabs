from .general_controller import GeneralController
from app.service import sellers_service
from flask_restful import Resource


class SellersController(GeneralController, Resource):
    _service = sellers_service
