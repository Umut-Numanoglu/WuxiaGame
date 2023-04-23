from game import db
from models import User
from models import Character


def create_tables():
    with db.engine.connect() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS characters (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                qi_cultivation INTEGER NOT NULL,
                cultivation_level INTEGER NOT NULL,
                inspiration INTEGER NOT NULL,
                health INTEGER NOT NULL,
                inventory VARCHAR(255) NOT NULL,
                alchemy_level INTEGER NOT NULL,
                artificier_level INTEGER NOT NULL,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
            )
        """)

    db.session.commit()
