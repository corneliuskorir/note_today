from flask import request, make_response
from ..models import Entry
from ..schemas import EntrySchema
from ..config import db
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class EntryResource(Resource):

    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)
        pagination = Entry.query.filter_by(user_id=user_id).paginate(
            page=page, per_page=per_page, error_out=False
        )
        entries = pagination.items

        if entries:
            return make_response(
                {
                    "page": page,
                    "per_page": per_page,
                    "total": pagination.total,
                    "total_pages": pagination.pages,
                    "items": EntrySchema(many=True).dump(entries),
                },
                200,
            )

        return make_response({"errors": ["No journal entries found."]}, 404)

    @jwt_required()
    def post(self):

        try:
            user_id = get_jwt_identity()

            data = {"user_id": user_id} | request.get_json()

            entry = EntrySchema().load(data=data)

            db.session.add(entry)
            db.session.commit()

            return make_response(EntrySchema().dump(entry), 201)
        except Exception as e:
            return make_response({"errors": [e]}, 404)
