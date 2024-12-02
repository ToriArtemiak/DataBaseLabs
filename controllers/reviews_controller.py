from .general_controller import GeneralController
from app.service import reviews_service
from flask_restful import Resource


class ReviewsController(GeneralController, Resource):
    _service = reviews_service
