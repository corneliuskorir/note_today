from flask import Blueprint

from flask_restful import Api
from .whoami import WhoAmI
from .login import LoginResource
from .signup import SignupResource
from .entry import EntryResource
from .entryid import EntryByIdResource

bp = Blueprint("api", __name__)
api = Api(bp)


api.add_resource(WhoAmI, "/me")
api.add_resource(LoginResource, "/login")
api.add_resource(SignupResource, "/signup")
api.add_resource(EntryResource, "/entries")
api.add_resource(EntryByIdResource, "/entries/<int:id>")
