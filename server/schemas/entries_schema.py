from marshmallow import Schema, fields, validate, post_load
from ..models import Entry


class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1))
    content = fields.String(required=True, validate=validate.Length(min=1))
    user_id = fields.Int(required=True)

    user = fields.Nested("UserSchema", exclude=("entries",))

    @post_load
    def to_entry(self, data, **kwargs):
        return Entry(**data)
