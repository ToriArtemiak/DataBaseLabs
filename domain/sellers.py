from __future__ import annotations
from app import db


class Seller(db.Model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    dealership_id = db.Column(db.Integer, db.ForeignKey('dealerships.id'))

    cars = db.relationship('Car', backref='seller', lazy=True)

    @staticmethod
    def create_from_dto(dto):
        return Seller(
            name=dto['name'],
            dealership_id=dto['dealership_id']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'dealership_id': self.dealership_id
        }
