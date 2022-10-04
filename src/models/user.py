from src.app import db
from src.app import flask_bcrypt


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    rol = db.Column(db.Integer, nullable=False)

    @property
    def password_public(self):
        raise AttributeError("password: write-only field")

    @password_public.setter
    def password_public(self, password):
        self.password = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)
