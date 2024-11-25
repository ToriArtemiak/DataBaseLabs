from __future__ import annotations
from app import db


class CarFeatureValue(db.Model):
    __tablename__ = 'car_feature_values'
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey('car_features.id'), primary_key=True)
    option_id = db.Column(db.Integer, db.ForeignKey('feature_options.id'))

    @staticmethod
    def create_from_dto(dto):
        return CarFeatureValue(
            car_id=dto['car_id'],
            feature_id=dto['feature_id'],
            option_id=dto['option_id']
        )

    def put_into_dto(self):
        return {
            'car_id': self.car_id,
            'feature_id': self.feature_id,
            'option_id': self.option_id
        }
