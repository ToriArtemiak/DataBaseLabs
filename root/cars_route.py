from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from .. import db
from ..controllers import cars_controller
from ..domain import CarFeature, FeatureOption, CarFeatureValue
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


@car_bp.route('/seller/<int:seller_id>/car', methods=['GET'])
def get_car_by_seller(seller_id: int):
    car = cars_controller.find_by_seller_id(seller_id)
    if not car:
        return make_response({"message": "No cars found for this seller"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify([{
        "id": car.id,
        "model": car.model,
        "brand": car.brand,
        "price": car.price,
        "country": car.country,
        "mileage": car.mileage,
        "year": car.year

    } for car in car]), HTTPStatus.OK)


@car_bp.route('/<int:car_id>/features', methods=['GET'])
def get_features_by_car(car_id: int):
    # Використовуємо SQLAlchemy ORM для виконання запиту
    car_features = (
        db.session.query(
            CarFeature.feature_name,
            FeatureOption.option_value
        )
        .join(CarFeatureValue, CarFeature.id == CarFeatureValue.feature_id)
        .join(FeatureOption, FeatureOption.id == CarFeatureValue.option_id)
        .filter(CarFeatureValue.car_id == car_id)
        .all()
    )

    if not car_features:
        return make_response({"message": "No features found for this car"}, HTTPStatus.NOT_FOUND)

    # Формуємо результат
    result = [
        {"feature_name": feature_name, "option_value": option_value}
        for feature_name, option_value in car_features
    ]

    return make_response(jsonify(result), HTTPStatus.OK)


@car_bp.route('/statistics_car', methods=['GET'])
def get_car_statistics():
    statistics = {
        "min_mileage": Car.get_min_mileage(),
        "max_mileage": Car.get_max_mileage(),
        "sum_mileage": Car.get_sum_mileage(),
        "avg_mileage": Car.get_avg_mileage(),
    }
    return make_response(jsonify(statistics), 200)
