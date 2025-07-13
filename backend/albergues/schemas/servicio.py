from utils.ma import ma
from marshmallow import fields

from models.servicio import Servicio
from schemas.albergue import Albergue_Schema

class Servicio_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Servicio
        include_fk = True
        fields = (
            'id_servicio',
            'nombre',
            'endpoint_api',
            'id_albergue',
            #'albergue'
        )
    
    #albergue = ma.Nested(Albergue_Schema)
    
servicio_schema = Servicio_Schema()
servicios_schema = Servicio_Schema(many=True)