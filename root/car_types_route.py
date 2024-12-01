from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import car_types_controller
from ..domain.car_types import CarType

car_type_bp = Blueprint('car_type', __name__, url_prefix='/car_type')

@car_type_bp.route('', methods=['GET'])
def get_all_car_types():
    return make_response(jsonify(car_types_controller.find_all()), HTTPStatus.OK)

@car_type_bp.route('', methods=['POST'])
def create_car_type() -> Response:
    content = request.get_json()
    car_type = CarType.create_from_dto(content)
    car_types_controller.create(car_type)
    return make_response(jsonify(car_type.put_into_dto()), HTTPStatus.CREATED)

@car_type_bp.route('/<int:car_type_id>', methods=['GET'])
def get_car_type(car_type_id: int) -> Response:
    car_type = car_types_controller.find_by_id(car_type_id)
    if car_type is None:
        return make_response({"message": "Car type not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(car_type), HTTPStatus.OK)

@car_type_bp.route('/<int:car_type_id>', methods=['PUT'])
def update_car_type(car_type_id: int) -> Response:
    content = request.get_json()
    car_type = CarType.create_from_dto(content)
    car_types_controller.update(car_type_id, car_type)
    return make_response("Car type updated", HTTPStatus.OK)

@car_type_bp.route('/<int:car_type_id>', methods=['PATCH'])
def patch_car_type(car_type_id: int) -> Response:
    content = request.get_json()
    car_types_controller.patch(car_type_id, content)
    return make_response("Car type updated", HTTPStatus.OK)

@car_type_bp.route('/<int:car_type_id>', methods=['DELETE'])
def delete_car_type(car_type_id: int) -> Response:
    car_types_controller.delete(car_type_id)
    return make_response("Car type deleted", HTTPStatus.OK)
