from flask import Blueprint
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from src.services import processing_data
from src.utils.utils import Roles

downloader = Blueprint('downloader', __name__)


@downloader.route("/download-data")
def download():
    verify_jwt_in_request()
    claims = get_jwt()
    # Solo Admin puede ver este endpoint
    if claims["role"] == str(Roles(1)):
        datas = processing_data.get_data_from_db()
        if datas:
            return {"message": "You already run this endpoint"}, 201
        processing_data.get_datas()
        return {"message": "Users saved successfully"}
    else:
        return {"message": "You don't have enough permissions to see this"}, 400
