from utils.ma import ma
from marshmallow import fields

from models.tipo_mascota import Tipo_mascota

class Tipo_mascota_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tipo_mascota
        include_fk = True
        fields = (
            'id_tipo_mascota',
            'nombre'
        )
        
tipo_mascota_schema = Tipo_mascota_Schema()
tipos_mascotas_schema = Tipo_mascota_Schema(many=True)