from utils.db import db

class Albergue(db.Model):
    __tablename__ = 'albergue'

    # Variables
    id_albergue = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    nombre = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    fec_creacion = db.Column(
        db.Date,
        nullable=False,
        default=db.func.current_date()
    )

    ubicacion = db.Column(
        Geometry('POINT'),
        nullable=False,
        unique=True
    )

    celular = db.Column(
        db.String(9),
        nullable=False,
        unique=True
    )

    # Constructor
    def __init__(self, 
                nombre,
                ubicacion,
                celular):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.celular=celular