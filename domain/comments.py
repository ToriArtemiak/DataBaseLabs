from __future__ import annotations
from app import db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    @staticmethod
    def create_from_dto(dto):
        return Comment(
            car_id=dto['car_id'],
            user_id=dto['user_id'],
            comment_text=dto['comment_text'],
            created_at=dto['created_at']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'user_id': self.user_id,
            'comment_text': self.comment_text,
            'created_at': self.created_at
        }
