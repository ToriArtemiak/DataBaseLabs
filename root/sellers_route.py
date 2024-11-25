from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import sellers_controller
from ..domain.sellers import Seller

seller_bp = Blueprint('seller', __name__, url_prefix='/seller')

@seller_bp.route('', methods=['GET'])
def get_all_sellers():
    return make_response(jsonify(sellers_controller.find_all()), HTTPStatus.OK)

@seller_bp.route('', methods=['POST'])
def create_seller() -> Response:
    content = request.get_json()
    seller = Seller.create_from_dto(content)
    sellers_controller.create(seller)
    return make_response(jsonify(seller.put_into_dto()), HTTPStatus.CREATED)

@seller_bp.route('/<int:seller_id>', methods=['GET'])
def get_seller(seller_id: int) -> Response:
    seller = sellers_controller.find_by_id(seller_id)
    if seller is None:
        return make_response({"message": "Seller not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(seller), HTTPStatus.OK)

@seller_bp.route('/<int:seller_id>', methods=['PUT'])
def update_seller(seller_id: int) -> Response:
    content = request.get_json()
    seller = Seller.create_from_dto(content)
    sellers_controller.update(seller_id, seller)
    return make_response("Seller updated", HTTPStatus.OK)

@seller_bp.route('/<int:seller_id>', methods=['PATCH'])
def patch_seller(seller_id: int) -> Response:
    content = request.get_json()
    sellers_controller.patch(seller_id, content)
    return make_response("Seller updated", HTTPStatus.OK)

@seller_bp.route('/<int:seller_id>', methods=['DELETE'])
def delete_seller(seller_id: int) -> Response:
    sellers_controller.delete(seller_id)
    return make_response("Seller deleted", HTTPStatus.OK)
