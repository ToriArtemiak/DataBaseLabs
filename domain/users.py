from __future__ import annotations
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    phone_number = db.Column(db.String(15), unique=True)

    @staticmethod
    def create_from_dto(dto):
        return User(
            username=dto['username'],
            email=dto['email'],
            password=dto['password'],
            phone_number=dto['phone_number']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'phone_number': self.phone_number
        }
