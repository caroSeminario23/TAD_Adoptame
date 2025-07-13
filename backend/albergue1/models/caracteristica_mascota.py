from utils.db import db

class Caracteristica_mascota(db.Model):
    __tablename__ = 'caracteristica_mascota'

    # Variables
    id_mascota = db.Column(
        db.Integer,
        db.ForeignKey('mascota.id_mascota'),
        primary_key=True,
        nullable=False
    )

    id_caracteristica = db.Column(
        db.Integer,
        db.ForeignKey('caracteristica_complementaria.id_caracteristica'),
        primary_key=True,
        nullable=False
    )

    valor = db.Column(
        db.String(25),
        nullable=False
    )

    # Relaciones
    caracteristica = db.relationship(
        'Caracteristica_complementaria',
        backref='car_complementaria_car_mascota'
    )

    mascota = db.relationship(
        'Mascota',
        backref='mascota_car_mascota'
    )

    # Constructor
    def __init__(self,
                id_mascota,
                id_caracteristica,
                valor):
        self.id_mascota = id_mascota
        self.id_caracteristica=id_caracteristica
        self.valor=valor