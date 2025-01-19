import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app


def create_token(username):
    now = datetime.now(tz=timezone.utc)
    payload = {
        'sub': username,
        'exp': now + timedelta(hours=1),
        'iat': now
    }
    token = {"token: ": jwt.encode(payload, current_app.config['JWT_SECRET_KEY'],
                                   algorithm='HS256'),
             "expires in: ": 3600,
             'issued at: ': now}
    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please try again.'
