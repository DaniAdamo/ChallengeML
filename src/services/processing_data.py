import requests
from src.models.data import Data
from src.app import db

URL = "https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios"


def get_datas():
    response = requests.get(URL)
    datas = response.json()
    save_data(datas)


def save_data(datas):
    for data in datas:
        d = Data(**data)
        db.session.add(d)
    db.session.commit()


def get_data_from_db():
    result = []
    for data in Data.query.all():
        result.append(data.as_dict())
    return result
