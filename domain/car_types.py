from __future__ import annotations
from app import db


class CarType(db.Model):
    __tablename__ = 'car_types'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255))

    @staticmethod
    def create_from_dto(dto):
        return CarType(
            type_name=dto['type_name']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'type_name': self.type_name
        }
