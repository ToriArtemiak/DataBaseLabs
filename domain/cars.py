from __future__ import annotations
from app import db
from sqlalchemy.sql import func
from sqlalchemy import Enum

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
    country = db.Column(db.String(255))
    mileage = db.Column(db.Integer)
    year = db.Column(db.Integer)
    car_type_id = db.Column(db.Integer, db.ForeignKey('car_types.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'))
    dealership_id = db.Column(db.Integer, db.ForeignKey('dealerships.id'))

    photos = db.relationship('CarPhoto', backref='car', lazy=True)
    comments = db.relationship('Comment', backref='car', lazy=True)

    @staticmethod
    def create_from_dto(dto):
        return Car(
            model=dto['model'],
            brand=dto['brand'],
            price=dto['price'],
            country=dto['country'],
            mileage=dto['mileage'],
            year=dto['year'],
            car_type_id=dto['car_type_id'],
            seller_id=dto['seller_id'],
            dealership_id=dto['dealership_id']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'model': self.model,
            'brand': self.brand,
            'price': self.price,
            'country': self.country,
            'mileage': self.mileage,
            'year': self.year,
            'car_type_id': self.car_type_id,
            'seller_id': self.seller_id,
            'dealership_id': self.dealership_id
        }


    @staticmethod
    def get_min_mileage() -> float:

        return db.session.query(func.min(Car.mileage)).scalar()

    @staticmethod
    def get_max_mileage() -> float:

        return db.session.query(func.max(Car.mileage)).scalar()

    @staticmethod
    def get_sum_mileage() -> float:

        return db.session.query(func.sum(Car.mileage)).scalar()

    @staticmethod
    def get_avg_mileage() -> float:

        return db.session.query(func.avg(Car.mileage)).scalar()

