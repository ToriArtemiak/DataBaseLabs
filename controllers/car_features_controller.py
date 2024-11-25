from .general_controller import GeneralController
from app.service import car_features_service
from flask_restful import Resource


class CarFeaturesController(GeneralController, Resource):
    _service = car_features_service
