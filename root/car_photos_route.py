from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import car_photos_controller
from ..domain.car_photos import CarPhoto

car_photo_bp = Blueprint('car_photo', __name__, url_prefix='/car_photo')

@car_photo_bp.route('', methods=['GET'])
def get_all_car_photos():
    return make_response(jsonify(car_photos_controller.find_all()), HTTPStatus.OK)

@car_photo_bp.route('', methods=['POST'])
def create_car_photo() -> Response:
    content = request.get_json()
    car_photo = CarPhoto.create_from_dto(content)
    car_photos_controller.create(car_photo)
    return make_response(jsonify(car_photo.put_into_dto()), HTTPStatus.CREATED)

@car_photo_bp.route('/<int:car_photo_id>', methods=['GET'])
def get_car_photo(car_photo_id: int) -> Response:
    car_photo = car_photos_controller.find_by_id(car_photo_id)
    if car_photo is None:
        return make_response({"message": "Car photo not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(car_photo), HTTPStatus.OK)

@car_photo_bp.route('/<int:car_photo_id>', methods=['PUT'])
def update_car_photo(car_photo_id: int) -> Response:
    content = request.get_json()
    car_photo = CarPhoto.create_from_dto(content)
    car_photos_controller.update(car_photo_id, car_photo)
    return make_response("Car photo updated", HTTPStatus.OK)

@car_photo_bp.route('/<int:car_photo_id>', methods=['PATCH'])
def patch_car_photo(car_photo_id: int) -> Response:
    content = request.get_json()
    car_photos_controller.patch(car_photo_id, content)
    return make_response("Car photo updated", HTTPStatus.OK)

@car_photo_bp.route('/<int:car_photo_id>', methods=['DELETE'])
def delete_car_photo(car_photo_id: int) -> Response:
    car_photos_controller.delete(car_photo_id)
    return make_response("Car photo deleted", HTTPStatus.OK)
