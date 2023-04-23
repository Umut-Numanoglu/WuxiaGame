from flask import jsonify, request
from werkzeug.security import check_password_hash

from services import UserService


class UserController:
    def __init__(self, app):
        self.user_service = UserService()

        @app.route("/api/user/register", methods=["POST"])
        def register():
            username = request.form.get("username")
            password = request.form.get("password")

            user = self.user_service.get_user_by_username(username)

            if not username or not password:
                return jsonify({"message": "Missing username or password"}), 400

            if user:
                return jsonify({"message": "User already exists"}), 409
            else:
                self.user_service.create_user(username, password)
                return jsonify({"message": "User created successfully"}), 201

        @app.route("/api/user/login", methods=["POST"])
        def login():
            username = request.form.get("username")
            password = request.form.get("password")

            if not username or not password:
                return jsonify({"message": "Missing username or password"}), 400

            user = self.user_service.get_user_by_username(username)

            if not user or not check_password_hash(user.password, password):
                return jsonify({"message": "Invalid username or password"}), 401

            # generate access token and return it as response
            access_token = user.generate_access_token()

            return jsonify({"access_token": access_token.decode("utf-8")}), 200
