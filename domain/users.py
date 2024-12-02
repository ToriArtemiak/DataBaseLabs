from __future__ import annotations
from app import db
from datetime import datetime
from random import randint, choice
from sqlalchemy.sql import text

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

    def insert_dummy_data():
        for i in range(1, 11):
            dummy_user = User(
                username=f"User{i}",
                email=f"user{i}@example.com",
                password=f"password{i}",
                phone_number=f"123456789{i}"
            )
            db.session.add(dummy_user)

        db.session.commit()

    @staticmethod
    def create_dynamic_tables_car():
        user_usernames = db.session.query(User.username).all()

        table_count = 0

        for username_tuple in user_usernames:
            if table_count >= 10:
                break

            user_username = username_tuple[0].replace(" ", "_")
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            table_name = f"{user_username}_{timestamp}"

            num_columns = randint(1, 9)

            columns_sql = []
            for i in range(1, num_columns + 1):
                col_name = f"col_{i}"
                col_type = choice(["VARCHAR(255)", "INT", "DECIMAL(10,2)", "DATE"])
                columns_sql.append(f"{col_name} {col_type}")

            columns_sql_str = ", ".join(columns_sql)
            create_table_sql = f"CREATE TABLE `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, {columns_sql_str});"

            db.session.execute(text(create_table_sql))
            print(f"Created table: {table_name}")

            table_count += 1

        db.session.commit()