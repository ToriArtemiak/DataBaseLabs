from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import feature_options_controller
from ..domain.feature_options import FeatureOption

feature_option_bp = Blueprint('feature_option', __name__, url_prefix='/feature_option')

@feature_option_bp.route('', methods=['GET'])
def get_all_feature_options():
    return make_response(jsonify(feature_options_controller.find_all()), HTTPStatus.OK)

@feature_option_bp.route('', methods=['POST'])
def create_feature_option() -> Response:
    content = request.get_json()
    feature_option = FeatureOption.create_from_dto(content)
    feature_options_controller.create(feature_option)
    return make_response(jsonify(feature_option.put_into_dto()), HTTPStatus.CREATED)

@feature_option_bp.route('/<int:feature_option_id>', methods=['GET'])
def get_feature_option(feature_option_id: int) -> Response:
    feature_option = feature_options_controller.find_by_id(feature_option_id)
    if feature_option is None:
        return make_response({"message": "Feature option not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(feature_option), HTTPStatus.OK)

@feature_option_bp.route('/<int:feature_option_id>', methods=['PUT'])
def update_feature_option(feature_option_id: int) -> Response:
    content = request.get_json()
    feature_option = FeatureOption.create_from_dto(content)
    feature_options_controller.update(feature_option_id, feature_option)
    return make_response("Feature option updated", HTTPStatus.OK)

@feature_option_bp.route('/<int:feature_option_id>', methods=['PATCH'])
def patch_feature_option(feature_option_id: int) -> Response:
    content = request.get_json()
    feature_options_controller.patch(feature_option_id, content)
    return make_response("Feature option updated", HTTPStatus.OK)

@feature_option_bp.route('/<int:feature_option_id>', methods=['DELETE'])
def delete_feature_option(feature_option_id: int) -> Response:
    feature_options_controller.delete(feature_option_id)
    return make_response("Feature option deleted", HTTPStatus.OK)
