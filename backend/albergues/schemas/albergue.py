from utils.ma import ma
from marshmallow import fields

from models.albergue import Albergue

class Albergue_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Albergue
        fields = (
            'id_albergue',
            'nombre',
            'fec_creacion',
            'ubicacion',
            'celular'
        )
albergue_schema = Albergue_Schema()
albergues_schema = Albergue_Schema(many=True)