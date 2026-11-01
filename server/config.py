from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_restful import Api

db = SQLAlchemy(metadata=MetaData())

api = Api()


def init_Api(app):
    global api
    api.init_app(app=app)
