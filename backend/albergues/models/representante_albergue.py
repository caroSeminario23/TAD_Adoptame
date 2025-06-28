from utils.db import db

class Representante_albergue(db.Model):
    __tablename__ = 'representante_albergue'

    # Variables
    id_representante = db.Column(
        db.Integer, 
        primary_key=True,
        autoincrement=True,
        nullable=False
    )

    nombres = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    apellidos = db.Column(
        db.String(50),
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
                nombres,
                apellidos,
                id_albergue):
        self.nombres=nombres
        self.apellidos=apellidos
        self.id_albergue=id_albergue