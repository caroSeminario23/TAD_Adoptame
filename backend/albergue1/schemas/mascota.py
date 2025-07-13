from utils.ma import ma
from marshmallow import fields

from models.mascota import Mascota

class Mascota_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mascota
        include_fk = True
        fields = (
            'id_mascota',
            'nombre',
            'foto',
            'fec_nacimiento',
            'sexo',
            'estatura',
            'peso',
            'id_tipo_mascota',
            'id_raza',
            'fec_ingreso',
            'adoptado',
            'discapacidad'
        )
        
mascota_schema = Mascota_Schema()
mascotas_schema = Mascota_Schema(many=True)