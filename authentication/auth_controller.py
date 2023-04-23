from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from services import UserService
from utils.security import generate_token, verify_token

auth_bp = Blueprint('auth', __name__)

user_service = UserService()


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # check if user with the same email or username already exists
    if user_service.get_user_by_email(email) is not None:
        return jsonify({'message': 'User with this email already exists.'}), 409
    if user_service.get_user_by_username(username) is not None:
        return jsonify({'message': 'User with this username already exists.'}), 409

    # create a new user object
    hashed_password = generate_password_hash(password, method='sha256')
    user = user_service.create_user(email=email, username=username, password=hashed_password)

    # generate a token for the new user
    token = generate_token(user.id)

    return jsonify({'token': token.decode('UTF-8')})


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # check if user with the given email exists
    user = user_service.get_user_by_email(email)
    if user is None:
        return jsonify({'message': 'User with this email does not exist.'}), 401

    # check if the password is correct
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Incorrect password.'}), 401

    # generate a token for the user
    token = generate_token(user.id)

    return jsonify({'token': token.decode('UTF-8')})


# logout endpoint
@auth_bp.route('/logout', methods=['POST'])
def logout():
    # get the token from the request header
    token = request.headers.get('Authorization')
    # verify the token
    payload = verify_token(token)
    if payload:
        # TODO: add code to handle logout
        return jsonify({'message': 'Logged out successfully'}), 200
    else:
        return jsonify({'message': 'Invalid token'}), 401


@auth_bp.route('/verify_token', methods=['POST'])
def verify_token():
    token = request.headers.get('Authorization').split(' ')[1]

    user_id = verify_token(token)
    if user_id is None:
        return jsonify({'message': 'Invalid token.'}), 401

    user = user_service.get_user_by_id(user_id)
    if user is None:
        return jsonify({'message': 'User not found.'}), 404

    return jsonify({'user_id': user_id})

