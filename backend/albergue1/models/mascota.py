from utils.db import db
from sqlalchemy.dialects.postgresql import TIMESTAMP

class Mascota(db.Model):
    __tablename__ = 'mascota'

    # Variables
    id_mascota = db.Column(
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

    foto = db.Column(
        db.Text,
        nullable=False
    )

    fec_nacimiento = db.Column(
        db.Date,
        nullable=False
    )

    sexo = db.Column(
        db.String(1),
        nullable=False
    )

    estatura = db.Column(
        db.Numeric(3,2),
        nullable=False
    )

    peso = db.Column(
        db.Numeric(5,2),
        nullable=False
    )

    id_tipo_mascota = db.Column(
        db.Integer,
        db.ForeignKey('tipo_mascota.id_tipo_mascota'),
        nullable=False
    )

    id_raza = db.Column(
        db.Integer,
        db.ForeignKey('raza.id_raza'),
        nullable=False
    )

    fec_ingreso = db.Column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )

    adoptado = db.Column(
        db.Boolean,
        nullable=False
    )

    discapacidad = db.Column(
        db.Boolean,
        nullable=False
    )

    # Relaciones
    tipo_mascota = db.relationship(
        'Tipo_mascota',
        backref='mascota_tipo_mascota'
    )

    raza = db.relationship(
        'Raza',
        backref='mascota_raza'
    )

    # Constructor
    def __init__(self, 
                 nombre,
                 foto,
                 fec_nacimiento,
                 sexo,
                 estatura,
                 peso,
                 id_tipo_mascota,
                 id_raza,
                 fec_ingreso,
                 adoptado,
                 discapacidad):
        self.nombre = nombre
        self.foto = foto
        self.fec_nacimiento = fec_nacimiento
        self.sexo = sexo
        self.estatura = estatura
        self.peso = peso
        self.id_tipo_mascota = id_tipo_mascota
        self.id_raza = id_raza
        self.fec_ingreso = fec_ingreso
        self.adoptado = adoptado
        self.discapacidad = discapacidad