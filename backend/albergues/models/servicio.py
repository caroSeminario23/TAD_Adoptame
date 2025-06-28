from utils.db import db

class Servicio(db.Model):
    __tablename__ = 'servicio'

    # Variables
    id_servicio = db.Column(
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

    endpoint_api = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )
    
    id_albergue = db.Column(
        db.Integer,
        db.ForeignKey('albergue.id_albergue'),
        nullable=False
    )

    # Relaciones
    albergue = db.relationship(
        'Albergue',
        backref='albergue_servicio'
    )

    # Constructor
    def __init__(self,
                nombre,
                endpoint_api,
                id_albergue):
        self.nombre=nombre
        self.endpoint_api=endpoint_api
        self.id_albergue=id_albergue