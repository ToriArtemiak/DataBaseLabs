import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://admin:password@127.0.0.1:3306/CarSalesDBLAB3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
