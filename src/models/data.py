from src.app import db
from sqlalchemy import func


class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    fec_alta = db.Column(db.String)
    user_name = db.Column(db.String)
    codigo_zip = db.Column(db.String)
    credit_card_num = db.Column(db.LargeBinary)
    credit_card_ccv = db.Column(db.LargeBinary)
    cuenta_numero = db.Column(db.String)
    direccion = db.Column(db.String)
    geo_latitud = db.Column(db.String)
    geo_longitud = db.Column(db.String)
    color_favorito = db.Column(db.String)
    foto_dni = db.Column(db.String)
    ip = db.Column(db.String)
    auto = db.Column(db.String)
    auto_modelo = db.Column(db.String)
    auto_tipo = db.Column(db.String)
    auto_color = db.Column(db.String)
    cantidad_compras_realizadas = db.Column(db.String)
    avatar = db.Column(db.String)
    fec_birthday = db.Column(db.String)

    @staticmethod
    def encrypt(data):
        return func.cifra(data)

    def __init__(self, id, fec_alta, user_name, codigo_zip, credit_card_num, credit_card_ccv, cuenta_numero,
                 direccion, geo_latitud, geo_longitud, color_favorito, foto_dni, ip, auto, auto_modelo,
                 auto_tipo, auto_color, cantidad_compras_realizadas, avatar, fec_birthday):
        self.fec_alta = fec_alta
        self.user_name = user_name
        self.codigo_zip = codigo_zip
        self.credit_card_num = self.encrypt(credit_card_num)
        self.credit_card_ccv = self.encrypt(credit_card_ccv)
        self.cuenta_numero = cuenta_numero
        self.direccion = direccion
        self.geo_latitud = geo_latitud
        self.geo_longitud = geo_longitud
        self.color_favorito = color_favorito
        self.foto_dni = foto_dni
        self.ip = ip
        self.auto = auto
        self.auto_modelo = auto_modelo
        self.auto_tipo = auto_tipo
        self.auto_color = auto_color
        self.cantidad_compras_realizadas = cantidad_compras_realizadas
        self.avatar = avatar
        self.fec_birthday = fec_birthday

    def as_dict(self):
        buffer = {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != "id" and c.name != "credit_card_num" and c.name != "credit_card_ccv"}
        buffer.update({"credit_card_num":"XXXX-XXXX-XXXX-XXXX","credit_card_ccv":"XXX"})
        return buffer