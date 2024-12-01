from .general_controller import GeneralController
from app.service import cars_service
from flask_restful import Resource


class CarsController(GeneralController, Resource):
    _service = cars_service
