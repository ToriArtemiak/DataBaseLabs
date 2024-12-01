from .general_controller import GeneralController
from app.service import car_types_service
from flask_restful import Resource


class CarTypesController(GeneralController, Resource):
    _service = car_types_service
