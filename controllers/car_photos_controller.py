from .general_controller import GeneralController
from app.service import car_photos_service
from flask_restful import Resource


class CarPhotosController(GeneralController, Resource):
    _service = car_photos_service
