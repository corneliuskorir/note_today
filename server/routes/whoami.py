from flask import make_response
from flask_restful import Resource

from ..models import User
from ..schemas import UserSchema
from flask_jwt_extended import get_jwt_identity, jwt_required


class WhoAmI(Resource):

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        user = User.query.filter_by(id=user_id).first()

        return make_response(UserSchema().dump(user), 200)
