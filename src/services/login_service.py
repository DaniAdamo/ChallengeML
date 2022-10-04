from src.models.user import User


def login (username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return 200, user.rol
    return 400, -1
