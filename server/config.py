from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_restful import Api
from flask_bcrypt import Bcrypt

db = SQLAlchemy(metadata=MetaData())

api = Api()
bcrypt = Bcrypt()


def init_Dependencies(app):
    global api
    global bcrypt
    api.init_app(app=app)
    bcrypt.init_app(app=app)
