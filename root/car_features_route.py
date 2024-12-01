from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import car_features_controller
from ..domain.car_features import CarFeature

car_feature_bp = Blueprint('car_feature', __name__, url_prefix='/car_feature')

@car_feature_bp.route('', methods=['GET'])
def get_all_car_features():
    return make_response(jsonify(car_features_controller.find_all()), HTTPStatus.OK)

@car_feature_bp.route('', methods=['POST'])
def create_car_feature() -> Response:
    content = request.get_json()
    car_feature = CarFeature.create_from_dto(content)
    car_features_controller.create(car_feature)
    return make_response(jsonify(car_feature.put_into_dto()), HTTPStatus.CREATED)

@car_feature_bp.route('/<int:car_feature_id>', methods=['GET'])
def get_car_feature(car_feature_id: int) -> Response:
    car_feature = car_features_controller.find_by_id(car_feature_id)
    if car_feature is None:
        return make_response({"message": "Car feature not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(car_feature), HTTPStatus.OK)

@car_feature_bp.route('/<int:car_feature_id>', methods=['PUT'])
def update_car_feature(car_feature_id: int) -> Response:
    content = request.get_json()
    car_feature = CarFeature.create_from_dto(content)
    car_features_controller.update(car_feature_id, car_feature)
    return make_response("Car feature updated", HTTPStatus.OK)

@car_feature_bp.route('/<int:car_feature_id>', methods=['PATCH'])
def patch_car_feature(car_feature_id: int) -> Response:
    content = request.get_json()
    car_features_controller.patch(car_feature_id, content)
    return make_response("Car feature updated", HTTPStatus.OK)

@car_feature_bp.route('/<int:car_feature_id>', methods=['DELETE'])
def delete_car_feature(car_feature_id: int) -> Response:
    car_features_controller.delete(car_feature_id)
    return make_response("Car feature deleted", HTTPStatus.OK)
