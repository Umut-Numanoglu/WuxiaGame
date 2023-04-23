from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from typing import List
from models import User, db


class UserService:
    def create_user(self, username: str, password: str, email: str) -> User:
        """Creates a new user with the given username, password, and email."""
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id: int) -> User:
        """Returns the user with the given ID."""
        return User.query.filter_by(id=user_id).first()

    def get_user_by_username(self, username: str) -> User:
        """Returns the user with the given username."""
        return User.query.filter_by(username=username).first()

    def check_password(self, user: User, password: str) -> bool:
        """Checks if the given password is correct for the given user."""
        return check_password_hash(user.password, password)

    def get_all_users(self) -> List[User]:
        """Returns a list of all users."""
        return User.query.all()

    def update_user(self, user: User, email: str = None, password: str = None) -> User:
        """Updates the given user's email and/or password."""
        if email is not None:
            user.email = email
        if password is not None:
            hashed_password = generate_password_hash(password)
            user.password = hashed_password
        db.session.commit()
        return user

    def delete_user(self, user: User) -> None:
        """Deletes the given user."""
        db.session.delete(user)
        db.session.commit()
