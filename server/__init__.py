from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import db, init_Dependencies
from .models import *
from .schemas import *
from .routes import bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "should-be-secrete"
    app.json.compact = False

    CORS(app=app)

    migrate = Migrate(app, db)
    db.init_app(app)
    init_Dependencies(app=app)
    JWTManager(app)

    app.register_blueprint(bp, url_prefix="/api")

    return app
