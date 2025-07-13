from utils.ma import ma
from marshmallow import fields

from models.caracteristica_mascota import Caracteristica_mascota

class Caracteristica_mascota_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Caracteristica_mascota
        include_fk = True
        fields = (
            'id_mascota',
            'id_caracteristica',
            'valor'
        )
        
caracteristica_mascota_schema = Caracteristica_mascota_Schema()
caracteristicas_mascotas_schema = Caracteristica_mascota_Schema(many=True)