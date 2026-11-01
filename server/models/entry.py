from server.config import db


class Entry(db.Model):

    __tablename__ = "entries"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True)
    content = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="entries")

    def __repr__(self):
        return f"<Entry {self.title} {self.id}>"
