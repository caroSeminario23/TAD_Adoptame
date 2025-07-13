from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.tipo_mascota import Tipo_mascota
from schemas.tipo_mascota import tipo_mascota_schema, tipos_mascotas_schema

tipo_mascota_routes = Blueprint('tipo_mascota_routes', __name__)

@tipo_mascota_routes.route("/get_tipos_mascotas", methods=["GET"])
def get_tipos_mascotas():
    tipos_mascotas = Tipo_mascota.query.all()

    if not tipos_mascotas:
        data = {
            'message': 'No se encontraron tipos de mascotas.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = tipos_mascotas_schema.dump(tipos_mascotas)
        data = {
            'message': 'Tipos de mascotas encontradas.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@tipo_mascota_routes.route("/get_tipo_mascota", methods=["POST"])
def get_tipo_mascota():
    id_tipo_mascota = request.json.get('id_tipo_mascota')
    if not id_tipo_mascota:
        data = {
            'message': 'ID de tipo de mascota no proporcionado.',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    else:
        tipo_mascota = Tipo_mascota.query.get(id_tipo_mascota)

        if not tipo_mascota:
            data = {
                'message': 'Tipo de mascota no encontrada.',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        else:
            result = tipo_mascota_schema.dump(tipo_mascota)
            data = {
                'message': 'Tipo de mascota encontrada.',
                'status': 200,
                'data': result
            }
            return make_response(jsonify(data), 200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              