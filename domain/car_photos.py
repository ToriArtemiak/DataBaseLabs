from __future__ import annotations
from app import db


class CarPhoto(db.Model):
    __tablename__ = 'car_photos'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    photo_url = db.Column(db.String(255))

    @staticmethod
    def create_from_dto(dto):
        return CarPhoto(
            car_id=dto['car_id'],
            photo_url=dto['photo_url']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'photo_url': self.photo_url
        }
