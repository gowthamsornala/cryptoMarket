from flask import request, Blueprint, jsonify
from app.oauth import create_token

bp = Blueprint('auth', __name__, url_prefix='/api/v1')

users = []


@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')

    if username in users:
        token = create_token(username)
        return jsonify({'token': token})
    else:
        response = {'error': 'Invalid username'}
        return jsonify(response), 401


@bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    if username in users:
        return jsonify({'error': 'User already exists'}), 400
    else:
        users.append(username)
        return jsonify({'message': 'User created successfully'}), 201
