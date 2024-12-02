from .general_service import GeneralService
from .. import db
from ..dao import cars_dao
from ..domain import CarFeature, FeatureOption, CarFeatureValue, Car


class CarService(GeneralService):
    _dao = cars_dao

    def find_by_seller_id(self, seller_id: int):
        return self._dao.find_by_seller_id(seller_id)

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
        return car_features

    def get_cars_by_feature(feature_id: int):
        # Використовуємо SQLAlchemy ORM для виконання запиту
        cars_with_feature = (
            db.session.query(
                Car.id,
                Car.model,
                Car.brand
            )
            .join(CarFeatureValue, CarFeatureValue.car_id == Car.id)
            .filter(CarFeatureValue.feature_id == feature_id)
            .all()
        )
        return cars_with_feature


