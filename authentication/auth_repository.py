from typing import Optional

from models import User
from sqlalchemy.orm import Session

from utils.security import hash_password


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, name: str, email: str, password: str) -> User:
        hashed_password = hash_password(password)
        user = User(name=name, email=email, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def check_user_exists(self, email: str) -> bool:
        user = self.get_user_by_email(email)
        return user is not None
