import secrets
import bcrypt
from datetime import datetime, timedelta
import jwt
from flask import current_app

def generate_token(length=32):
    """Generate a random token of the specified length."""
    return secrets.token_hex(length)

def hash_password(password):
    """Hash a password using the bcrypt algorithm."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed_password):
    """Verify a password against a hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def verify_token(token):
    try:
        # decode the token using the app secret key
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        # check if the token is expired
        exp = datetime.fromtimestamp(payload['exp'])
        if exp < datetime.utcnow():
            return None
        # return the decoded payload
        return payload
    except:
        return None