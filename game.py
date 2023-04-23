from utils.util import create_tables
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask import Flask
from injector import Binder
from utils.database import Database
from authentication.auth_controller import AuthController
from authentication.auth_repository import AuthRepository
from characters.character_controller import CharacterController
from characters.character_repository import CharacterRepository
from inventory.inventory_controller import InventoryController
from inventory.inventory_repository import InventoryRepository
from cultivation.cultivation_controller import CultivationController
from cultivation.cultivation_repository import CultivationRepository
from users.users_controller import UsersController
from users.users_repository import UsersRepository


def configure(binder: Binder) -> Binder:
    binder.bind(Database, to=Database())
    binder.bind(AuthController, to=AuthController())
    binder.bind(AuthRepository, to=AuthRepository())
    binder.bind(CharacterController, to=CharacterController())
    binder.bind(CharacterRepository, to=CharacterRepository())
    binder.bind(InventoryController, to=InventoryController())
    binder.bind(InventoryRepository, to=InventoryRepository())
    binder.bind(CultivationController, to=CultivationController())
    binder.bind(CultivationRepository, to=CultivationRepository())
    return binder


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'RFGSDFGS§$%§sdf34rtsdfs§"$'  # Replace with your own secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
# Create tables at startup
with app.app_context():
    db.create_all()
    create_tables()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
