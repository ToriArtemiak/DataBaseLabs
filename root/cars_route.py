from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import cars_controller
from ..domain.cars import Car

car_bp = Blueprint('car', __name__, url_prefix='/car')

@car_bp.route('', methods=['GET'])
def get_all_cars():
    return make_response(jsonify(cars_controller.find_all()), HTTPStatus.OK)

@car_bp.route('', methods=['POST'])
def create_car() -> Response:
    content = request.get_json()
    car = Car.create_from_dto(content)
    cars_controller.create(car)
    return make_response(jsonify(car.put_into_dto()), HTTPStatus.CREATED)

@car_bp.route('/<int:car_id>', methods=['GET'])
def get_car(car_id: int) -> Response:
    car = cars_controller.find_by_id(car_id)
    if car is None:
        return make_response({"message": "Car not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(car), HTTPStatus.OK)

@car_bp.route('/<int:car_id>', methods=['PUT'])
def update_car(car_id: int) -> Response:
    content = request.get_json()
    car = Car.create_from_dto(content)
    cars_controller.update(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)

@car_bp.route('/<int:car_id>', methods=['PATCH'])
def patch_car(car_id: int) -> Response:
    content = request.get_json()
    cars_controller.patch(car_id, content)
    return make_response("Car updated", HTTPStatus.OK)

@car_bp.route('/<int:car_id>', methods=['DELETE'])
def delete_car(car_id: int) -> Response:
    cars_controller.delete(car_id)
    return make_response("Car deleted", HTTPStatus.OK)
