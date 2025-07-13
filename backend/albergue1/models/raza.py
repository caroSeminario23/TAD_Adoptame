from utils.db import db

class Raza(db.Model):
    __tablename__ = 'raza'

    # Variables
    id_raza = db.Column(
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