from .general_controller import GeneralController
from app.service import car_feature_values_service
from flask_restful import Resource


class CarFeatureValuesController(GeneralController, Resource):
    _service = car_feature_values_service
