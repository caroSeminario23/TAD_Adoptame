from utils.ma import ma
from marshmallow import fields

from models.representante_albergue import Representante_albergue
from schemas.albergue import Albergue_Schema

class Representante_albergue_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Representante_albergue
        fields = (
            'id_representante',
            'nombres',
            'apellidos',
            'id_albergue',
            'albergue'
        )
    
    albergue = ma.Nested(Albergue_Schema)
    
representante_albergue_schema = Representante_albergue_Schema()
representantes_albergues_schema = Representante_albergue_Schema(many=True)