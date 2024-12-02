from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from .. import db
from ..controllers import reviews_controller
from ..domain.reviews import Review


review_bp = Blueprint('review', __name__, url_prefix='/review')

@review_bp.route('', methods=['GET'])
def get_all_reviews() -> Response:

    return make_response(jsonify(reviews_controller.find_all()), HTTPStatus.OK)

@review_bp.route('', methods=['POST'])
def create_review() -> Response:
    """
    Create a new review.
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    reviews_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)

def insert_review(car_id: int, review_text:str, rating:float) -> Review:
    new_review = Review(
        car_id=car_id,
        review_text=review_text,
        rating=rating
    )
    db.session.add(new_review)
    db.session.commit()
    return new_review


@review_bp.route('/parametrized', methods=['POST'])
def insert_parametrized() -> Response:
    content = request.get_json()
    new_review = insert_review(
        car_id = content['car_id'],
        review_text = content['review_text'],
        rating = content['rating']
    )
    return make_response(jsonify(new_review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id: int) -> Response:
    """
    Fetch a single review by ID.
    """
    review = reviews_controller.find_by_id(review_id)
    if review is None:
        return make_response({"message": "Review not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(review), HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id: int) -> Response:
    """
    Update an existing review (overwrite).
    """
    content = request.get_json()
    review = Review.create_from_dto(content)
    reviews_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=['PATCH'])
def patch_review(review_id: int) -> Response:
    """
    Partially update a review.
    """
    content = request.get_json()
    reviews_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id: int) -> Response:
    """
    Delete a review by ID.
    """
    reviews_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
