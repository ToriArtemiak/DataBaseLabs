from .general_controller import GeneralController
from app.service import feature_options_service
from flask_restful import Resource


class FeatureOptionsController(GeneralController, Resource):
    _service = feature_options_service
