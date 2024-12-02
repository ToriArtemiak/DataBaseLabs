from __future__ import annotations
from app import db


class Dealership(db.Model):
    __tablename__ = 'dealerships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))

    sellers = db.relationship('Seller', backref='dealership', lazy=True)

    @staticmethod
    def create_from_dto(dto):
        return Dealership(
            name=dto['name'],
            location=dto['location']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }
