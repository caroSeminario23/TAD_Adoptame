from utils.ma import ma
from marshmallow import fields

from models.raza import Raza

class Raza_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Raza
        include_fk = True
        fields = (
            'id_raza',
            'nombre'
        )
        
raza_schema = Raza_Schema()
razas_schema = Raza_Schema(many=True)