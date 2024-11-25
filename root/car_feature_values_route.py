from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import car_feature_values_controller
from ..domain.car_feature_values import CarFeatureValue

car_feature_value_bp = Blueprint('car_feature_value', __name__, url_prefix='/car_feature_value')

@car_feature_value_bp.route('', methods=['GET'])
def get_all_car_feature_values():
    return make_response(jsonify(car_feature_values_controller.find_all()), HTTPStatus.OK)

@car_feature_value_bp.route('', methods=['POST'])
def create_car_feature_value() -> Response:
    content = request.get_json()
    car_feature_value = CarFeatureValue.create_from_dto(content)
    car_feature_values_controller.create(car_feature_value)
    return make_response(jsonify(car_feature_value.put_into_dto()), HTTPStatus.CREATED)

@car_feature_value_bp.route('/<int:car_feature_value_id>', methods=['GET'])
def get_car_feature_value(car_feature_value_id: int) -> Response:
    car_feature_value = car_feature_values_controller.find_by_id(car_feature_value_id)
    if car_feature_value is None:
        return make_response({"message": "Car feature value not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(car_feature_value), HTTPStatus.OK)

@car_feature_value_bp.route('/<int:car_feature_value_id>', methods=['PUT'])
def update_car_feature_value(car_feature_value_id: int) -> Response:
    content = request.get_json()
    car_feature_value = CarFeatureValue.create_from_dto(content)
    car_feature_values_controller.update(car_feature_value_id, car_feature_value)
    return make_response("Car feature value updated", HTTPStatus.OK)

@car_feature_value_bp.route('/<int:car_feature_value_id>', methods=['PATCH'])
def patch_car_feature_value(car_feature_value_id: int) -> Response:
    content = request.get_json()
    car_feature_values_controller.patch(car_feature_value_id, content)
    return make_response("Car feature value updated", HTTPStatus.OK)

@car_feature_value_bp.route('/<int:car_feature_value_id>', methods=['DELETE'])
def delete_car_feature_value(car_feature_value_id: int) -> Response:
    car_feature_values_controller.delete(car_feature_value_id)
    return make_response("Car feature value deleted", HTTPStatus.OK)
