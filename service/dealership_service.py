from .general_service import GeneralService
from ..dao import dealership_dao
from app import db
from ..domain.cars import Car
from ..domain.dealership import Dealership
class DealershipService(GeneralService):
    _dao = dealership_dao




# Проміжна таблиця для зв’язку Cars і Dealerships
class CarDealership(db.Model):
    __tablename__ = 'car_dealerships'
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), primary_key=True)
    dealership_id = db.Column(db.Integer, db.ForeignKey('dealerships.id'), primary_key=True)


class CarDealershipService:
    @staticmethod
    def add_car_to_dealership(car_model: str, dealership_name: str) -> CarDealership:
        # Пошук автомобіля
        car = Car.query.filter_by(model=car_model).first()
        if not car:
            raise ValueError("Car not found")

        # Пошук дилера
        dealership = Dealership.query.filter_by(name=dealership_name).first()
        if not dealership:
            raise ValueError("Dealership not found")

        # Створення зв’язку
        car_dealership = CarDealership(car_id=car.id, dealership_id=dealership.id)
        db.session.add(car_dealership)
        db.session.commit()

        return car_dealership


