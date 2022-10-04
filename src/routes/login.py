from flask import Blueprint, jsonify, request
from src.services import login_service
from flask_jwt_extended import create_access_token
from src.utils.utils import Roles

loger = Blueprint('loger', __name__)


@loger.route("/login", methods=["POST"])
def show():
    data = request.get_json()
    result, rol = login_service.login(data["username"], data["password"])
    if result == 200:
        access_token = create_access_token(
           identity=data.get("username"),
           additional_claims={"role": str(Roles(rol))})
        response = jsonify(access_token=access_token)
        response.status_code = 200
        return response
    else:
        response = jsonify(
           status="fail",
           message=f"Something wrong.",
        )
        response.status_code = 400
        return response
