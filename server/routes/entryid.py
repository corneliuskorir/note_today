from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..config import db
from ..models import Entry
from ..schemas import EntrySchema


class EntryByIdResource(Resource):
    @jwt_required()
    def patch(self, id):

        entry = Entry.query.filter_by(id=id).first()
        if not entry:
            return make_response({"errors": ["No entry found"]}, 404)

        for key, value in request.get_json().items():
            if hasattr(entry, key):
                setattr(entry, key, value)

        db.session.commit()
        return make_response(EntrySchema().dump(entry), 200)

    @jwt_required()
    def delete(self, id):
        entry = Entry.query.filter_by(id=id).first()

        if not entry:
            make_response({"errors": ["No entry found"]}, 404)

        db.session.delete(entry)
        db.session.commit()
        return make_response({}, 204)
