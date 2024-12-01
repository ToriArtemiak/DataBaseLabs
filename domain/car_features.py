from __future__ import annotations
from app import db


class CarFeature(db.Model):
    __tablename__ = 'car_features'
    id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.String(255))

    @staticmethod
    def create_from_dto(dto):
        return CarFeature(
            feature_name=dto['feature_name']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'feature_name': self.feature_name
        }
