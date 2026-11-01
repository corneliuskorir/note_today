from marshmallow import Schema, fields, validate, pre_load
from ..models import Entry


class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1))
    content = fields.String(required=True, validate=validate.Length(min=1))
    user = fields.Nested("UserSchema", exclude=("entries",))

    @pre_load
    def to_entry(self, data, **kwargs):
        return Entry(**data)
