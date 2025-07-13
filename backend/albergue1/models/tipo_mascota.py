from utils.db import db

class Tipo_mascota(db.Model):
    __tablename__ = 'tipo_mascota'

    # Variables
    id_tipo_mascota = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    nombre = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    # Constructor
    def __init__(self,
                nombre):
        self.nombre=nombre