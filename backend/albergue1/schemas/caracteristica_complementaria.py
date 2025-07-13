from utils.ma import ma
from marshmallow import fields

from models.caracteristica_complementaria import Caracteristica_complementaria

class Caracteristica_complementaria_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Caracteristica_complementaria
        include_fk = True
        fields = (
            'id_caracteristica',
            'nombre',
            'unidad_medida'
        )
        
caracteristica_complementaria_schema = Caracteristica_complementaria_Schema()
caracteristicas_complementarias_schema = Caracteristica_complementaria_Schema(many=True)