from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models.users import User

db = SQLAlchemy()


class UserRepository:
    @staticmethod
    def create_user(email: str, password: str) -> User:
        hashed_password = generate_password_hash(password)
        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter_by(email=email).first()

    @staticmethod
    def check_password(user: User, password: str) -> bool:
        return check_password_hash(user.password, password)

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get(user_id)

