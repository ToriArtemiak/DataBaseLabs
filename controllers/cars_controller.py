from .general_controller import GeneralController
from app.service import cars_service
from flask_restful import Resource


class CarsController(GeneralController, Resource):
    _service = cars_service

    def find_by_seller_id(self, seller_id: int):
        return self._service.find_by_seller_id(seller_id)

    def find_features_by_car(self, car_id: int):
        return cars_service.get_features_by_car(car_id)

    def find_cars_by_feature(self, feature_id: int):
        return cars_service.get_cars_by_feature(feature_id)
