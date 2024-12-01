from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import dealership_controller
from ..domain.dealership import Dealership

dealership_bp = Blueprint('dealership', __name__, url_prefix='/dealership')


@dealership_bp.route('', methods=['GET'])
def get_all_dealerships():
    return make_response(jsonify(dealership_controller.find_all()), HTTPStatus.OK)


@dealership_bp.route('', methods=['POST'])
def create_dealership() -> Response:
    content = request.get_json()
    dealership = Dealership.create_from_dto(content)
    dealership_controller.create(dealership)
    return make_response(jsonify(dealership.put_into_dto()), HTTPStatus.CREATED)


@dealership_bp.route('/<int:dealership_id>', methods=['GET'])
def get_dealership(dealership_id: int) -> Response:
    dealership = dealership_controller.find_by_id(dealership_id)
    if dealership is None:
        return make_response({"message": "Dealership not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(dealership), HTTPStatus.OK)


@dealership_bp.route('/<int:dealership_id>', methods=['PUT'])
def update_dealership(dealership_id: int) -> Response:
    content = request.get_json()
    dealership = Dealership.create_from_dto(content)
    dealership_controller.update(dealership_id, dealership)
    return make_response("Dealership updated", HTTPStatus.OK)


@dealership_bp.route('/<int:dealership_id>', methods=['PATCH'])
def patch_dealership(dealership_id: int) -> Response:
    content = request.get_json()
    dealership_controller.patch(dealership_id, content)
    return make_response("Dealership updated", HTTPStatus.OK)


@dealership_bp.route('/<int:dealership_id>', methods=['DELETE'])
def delete_dealership(dealership_id: int) -> Response:
    dealership_controller.delete(dealership_id)
    return make_response("Dealership deleted", HTTPStatus.OK)
