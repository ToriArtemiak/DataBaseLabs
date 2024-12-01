from __future__ import annotations
from app import db


class FeatureOption(db.Model):
    __tablename__ = 'feature_options'
    id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey('car_features.id'))
    option_value = db.Column(db.String(255))

    @staticmethod
    def create_from_dto(dto):
        return FeatureOption(
            feature_id=dto['feature_id'],
            option_value=dto['option_value']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'feature_id': self.feature_id,
            'option_value': self.option_value
        }
