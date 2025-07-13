from utils.db import db

class Caracteristica_complementaria(db.Model):
    __tablename__ = 'caracteristica_complementaria'

    # Variables
    id_caracteristica = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    nombre = db.Column(
        db.String(15),
        nullable=False,
        unique=True
    )

    unidad_medida = db.Column(
        db.String(7),
        nullable=False
    )

    # Constructor
    def __init__(self,
                nombre,
                unidad_medida):
        self.nombre=nombre
        self.unidad_medida=unidad_medida