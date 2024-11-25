from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import comments_controller
from ..domain.comments import Comment

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

@comment_bp.route('', methods=['GET'])
def get_all_comments():
    return make_response(jsonify(comments_controller.find_all()), HTTPStatus.OK)

@comment_bp.route('', methods=['POST'])
def create_comment() -> Response:
    content = request.get_json()
    comment = Comment.create_from_dto(content)
    comments_controller.create(comment)
    return make_response(jsonify(comment.put_into_dto()), HTTPStatus.CREATED)

@comment_bp.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id: int) -> Response:
    comment = comments_controller.find_by_id(comment_id)
    if comment is None:
        return make_response({"message": "Comment not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(comment), HTTPStatus.OK)

@comment_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id: int) -> Response:
    content = request.get_json()
    comment = Comment.create_from_dto(content)
    comments_controller.update(comment_id, comment)
    return make_response("Comment updated", HTTPStatus.OK)

@comment_bp.route('/<int:comment_id>', methods=['PATCH'])
def patch_comment(comment_id: int) -> Response:
    content = request.get_json()
    comments_controller.patch(comment_id, content)
    return make_response("Comment updated", HTTPStatus.OK)


@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id: int) -> Response:
    comments_controller.delete(comment_id)
    return make_response("Comment deleted", HTTPStatus.OK)
