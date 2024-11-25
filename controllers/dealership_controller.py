from .general_controller import GeneralController
from app.service import dealership_service
from flask_restful import Resource


class DealershipController(GeneralController, Resource):
    _service = dealership_service
