from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.sessionmaker()
