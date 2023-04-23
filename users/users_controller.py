from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest, NotFound

from services import UserService
from utils.security import generate_token, verify_password


class UsersController(Resource):
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def post(self):
        data = request.get_json()

        if not data:
            raise BadRequest("No input data provided")

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise BadRequest("Invalid input data")

        user = self.user_service.create_user(username, password)

        return {"message": "User created successfully", "data": {"id": user.id, "username": user.username}}, 201

    def login(self):
        data = request.get_json()

        if not data:
            raise BadRequest("No input data provided")

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise BadRequest("Invalid input data")

        user = self.user_service.get_user_by_username(username)

        if not user or not verify_password(password, user.password):
            raise NotFound("Invalid username or password")

        token = generate_token(user.id)

        return {"message": "User logged in successfully", "data": {"token": token.decode("utf-8")}}, 200
