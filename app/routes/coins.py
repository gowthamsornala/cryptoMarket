from flask import Blueprint, request, jsonify, current_app
import requests
from app import oauth

bp = Blueprint('coins', __name__, url_prefix='/api/v1/coins')
api_key = current_app.config['COINGECKO_API_KEY']


@bp.route('/', methods=['GET'])
def list_coins():
    try:
        token = request.headers.get('Authorization').split(' ')[1]
    except Exception as e:
        print(f'Exception: {e}')
        response = {'error': 'Token is missing'}
        return jsonify(response), 400
    decode_result = oauth.decode_token(token)
    if decode_result in ['Signature expired. Please log in again.',
                         'Invalid token. Please try again.']:
        return jsonify({'error': decode_result}), 401
    else:
        url = "https://api.coingecko.com/api/v3/coins/list"
        headers = {"accept": "application/json",
                   "x-cg-demo-api-key": api_key
                   }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            page_num = int(request.args.get('page_num', 1))
            per_page = min(int(request.args.get('per_page',
                                                current_app.config['PAGINATION_DEFAULT'])),
                           current_app.config['PAGINATION_MAX'])
            start_index = (page_num-1)*per_page
            json_response = [{'id': coin['id'], 'name': coin['name']}
                             for coin in response.json()]
            return jsonify(json_response[start_index:start_index+per_page])
        else:
            response = {'error': 'Unable to fetch coins from CoinGecko API'}
            return jsonify(response)


@bp.route('/<string:coin_id>', methods=['GET'])
def get_coin(coin_id):
    # Implement logic to fetch specific coin details from CoinGecko API
    try:
        token = request.headers.get('Authorization').split(' ')[1]
    except Exception as e:
        print(f'Exception: {e}')
        response = {'error': 'Token is missing'}
        return jsonify(response), 400
    decode_result = oauth.decode_token(token)
    if decode_result in ['Signature expired. Please log in again.',
                         'Invalid token. Please try again.']:
        return jsonify({'error': decode_result}), 401
    else:
        url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
        headers = {"accept": "application/json",
                   "x-cg-demo-api-key": api_key}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            json_response = response.json()
            return jsonify(json_response)
        else:
            response = {'error': 'Unable to fetch coin data from CoinGecko API'}
            return jsonify(response)
