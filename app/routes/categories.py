from flask import Blueprint, request, jsonify, current_app
import requests
from app import oauth

bp = Blueprint('categories', __name__, url_prefix='/api/v1/categories')
api_key = current_app.config['COINGECKO_API_KEY']


@bp.route('/', methods=['GET'])
def list_categories():
    # Implement logic to fetch categories from CoinGecko API
    try:
        token = request.headers.get('Authorization').split(' ')[1]
    except Exception as e:
        print(f'Exception: {e}')
        return jsonify({'error': 'Token is missing'}), 400
    decode_result = oauth.decode_token(token)
    if decode_result in ['Signature expired. Please log in again.',
                         'Invalid token. Please try again.']:
        return jsonify({'error': decode_result}), 401
    else:
        url = 'https://api.coingecko.com/api/v3/coins/categories/list'
        headers = {"accept": "application/json",
                   "x-cg-demo-api-key": api_key}
        page_num = int(request.args.get('page_num', 1))
        per_page = min(int(request.args.get('per_page',
                                            current_app.config['PAGINATION_DEFAULT'])),
                       current_app.config['PAGINATION_MAX'])
        start_index = (page_num-1) * per_page
        response = requests.get(url, headers=headers)
        json_response = [{'id': category['category_id'], 'name': category['name']}
                         for category in response.json()]
        # json_response = response.json()
        return jsonify(json_response[start_index:start_index+per_page])
