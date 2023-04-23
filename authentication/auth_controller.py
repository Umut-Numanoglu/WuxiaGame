from flask import request, jsonify
from werkzeug.security import check_password_hash

from game import app
from services import UserService
from utils.security import generate_token, verify_token


class AuthController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    @app.route('/login', methods=['POST'])
    def login(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

        user = self.user_service.get_user_by_username(auth.username)
        if not user:
            return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

        if check_password_hash(user.password, auth.password):
            token = generate_token(user.id)
            return jsonify({'token': token.decode('UTF-8')})

        return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    @app.route('/register', methods=['POST'])
    def register(self):

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')

        if not email or not password or not name:
            return jsonify({'message': 'All fields are required'}), 400

        user = self.user_service.get_user_by_username(data['username'])
        if user:
            return jsonify({'message': 'Username already exists'}), 400

        if len(password) < 6:
            return jsonify({'message': 'Password must be at least 6 characters long'}), 400

        user_service = UserService()
        user = user_service.create_user(email=email, password=password, username=name)

        return jsonify({'message': 'User created successfully', 'user_id': user.id}), 201

    @app.route('/logout', methods=['POST'])
    def logout(self):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Missing Authorization header'}), 401

        try:
            user_id = verify_token(token)
            if user_id:
                return jsonify({'message': 'Successfully logged out'}), 200
            else:
                return jsonify({'message': 'Invalid token, failed to logout'}), 401

        except Exception as e:
            print(e)
            return jsonify({'message': 'Invalid token, failed to logout'}), 401
