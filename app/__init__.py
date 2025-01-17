from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    #     "SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "RENDER_DATABASE_URI")
    
    app.config["SLACK_API_TOKEN_URI"] = os.environ.get("SLACK_API_TOKEN_URI")

    from app.models.board import Board
    from app.models.card import Card

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.board_routes import board_bp
    app.register_blueprint(board_bp)

    from .routes.card_routes import bp
    app.register_blueprint(bp)

    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    return app
