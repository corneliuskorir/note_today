from flask import Flask
from flask_migrate import Migrate

from .config import db, init_Dependencies
from .models import *


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///note.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    migrate = Migrate(app, db)
    db.init_app(app)
    init_Dependencies(app=app)

    return app
