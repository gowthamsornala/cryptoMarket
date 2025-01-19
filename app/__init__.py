from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['COINGECKO_API_KEY'] = os.environ.get('COINGECKO_API_KEY')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    with app.app_context():
        from .routes import coins, categories, auth
        app.register_blueprint(coins.bp)
        app.register_blueprint(categories.bp)
        app.register_blueprint(auth.bp)

    return app
