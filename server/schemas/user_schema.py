from marshmallow import Schema, fields, validate, pre_load

from ..models import User


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String(validate=validate.Length(min=1))
    entries = fields.Nested("EntriesSchema", many=True, exclude="user")

    @pre_load
    def to_user(self, data, **kwargs):
        return User(**data)
