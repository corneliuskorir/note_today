from server.config import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    entries = db.relationship("Entry", back_populates="user", cascade="all,delete")

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewd.")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password=password.encode("utf-8")
        )

    def __repr__(self):
        return f"<User {self.username}>"
