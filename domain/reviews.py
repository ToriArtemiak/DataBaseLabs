from __future__ import annotations


from app import db


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    cars = db.relationship('Car', backref='review', lazy=True)

    @staticmethod
    def create_from_dto(dto):
        return Review(
            car_id=dto['car_id'],
            review_text=dto['review_text'],
            rating=dto['rating']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'car_id': self.car_id,
            'review_text': self.review_text,
            'rating': self.rating,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
