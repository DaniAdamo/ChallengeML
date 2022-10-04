from flask import Blueprint, jsonify
from src.services import processing_data
from src.app import flask_bcrypt
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt
from src.utils.utils import Roles

shower = Blueprint('shower', __name__)


@shower.route("/")
@jwt_required()
def show():
    verify_jwt_in_request()
    claims = get_jwt()
    # Roles Admin y Reader pueden ver este endpoint
    if claims["role"] in (str(Roles(1)), str(Roles(2))):
        datas = processing_data.get_data_from_db()
        if datas:
            return jsonify(datas), 200
        else:
            return {"message": "No data downloaded try in /download-data endpoint"}, 202
    return {"message": "You don't have enough permissions to see this"}, 400
