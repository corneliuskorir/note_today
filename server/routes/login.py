from flask_restful import Resource
from flask import request, make_response
from ..models import User
from ..schemas import UserSchema
from flask_jwt_extended import create_access_token, jwt_required


class LoginResource(Resource):
    def post(self):
        username = request.get_json()["username"]
        password = request.get_json()["password"]

        user: User = User.query.filter_by(username=username).first()
        if user and user.authenticate(password=password):

            token = create_access_token(identity=str(user.id))

            return make_response({"token": token, "user": UserSchema().dump(user)}, 200)

        return make_response({"errors": ["Invalid username or password"]}, 401)
