from flask import request, make_response
from flask_restful import Resource
from ..models import User
from ..schemas import UserSchema

from ..config import db
from flask_jwt_extended import create_access_token


class SignupResource(Resource):
    def post(self):
        username = request.get_json()["username"]
        password = request.get_json()["password"]
        confirm_password = request.get_json()["password_confirmation"]

        try:
            if password == confirm_password:
                new_user = User(username=username)
                new_user.password_hash = password

                db.session.add(new_user)
                db.session.commit()
                print("Generated user id:", new_user.id)
                token = create_access_token(identity=str(new_user.id))

                return make_response(
                    {"token": token, "user": UserSchema().dump(new_user)}, 201
                )

            raise Exception("Passwords dont match.")
        except Exception as e:
            return make_response({"errors": [f"{e}"]}, 404)
