from .general_controller import GeneralController
from app.service import comments_service
from flask_restful import Resource


class CommentsController(GeneralController, Resource):
    _service = comments_service
