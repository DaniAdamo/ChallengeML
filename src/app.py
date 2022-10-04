from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import configuration
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
flask_bcrypt = Bcrypt()
jwt = JWTManager()

# To be taken for Migrate()
from src.models.user import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(configuration['development'])
    db.init_app(app)
    migrate.init_app(app, db)
    flask_bcrypt.init_app(app)
    jwt.init_app(app)
    return app

