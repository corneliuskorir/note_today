from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt

db = SQLAlchemy(metadata=MetaData())

bcrypt = Bcrypt()


def init_Dependencies(app):
    global api
    global bcrypt
    bcrypt.init_app(app=app)
