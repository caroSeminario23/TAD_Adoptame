from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.mascota import Mascota
from schemas.mascota import mascota_schema, mascotas_schema

mascota_routes = Blueprint('mascota_routes', __name__)

@mascota_routes.route("/get_mascotas", methods=["GET"])
def get_mascotas():
    mascotas = Mascota.query.all()

    if not mascotas:
        data = {
            'message': 'No se encontraron mascotas.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = mascotas_schema.dump(mascotas)
        data = {
            'message': 'Mascotas encontradas.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@mascota_routes.route("/get_mascota", methods=["POST"])
def get_mascota():
    id_mascota = request.json.get('id_mascota')
    if not id_mascota:
        data = {
            'message': 'ID de mascota no proporcionado.',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    else:
        mascota = Mascota.query.get(id_mascota)

        if not mascota:
            data = {
                'message': 'Mascota no encontrada.',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        else:
            result = mascota_schema.dump(mascota)
            data = {
                'message': 'Mascota encontrada.',
                'status': 200,
                'data': result
            }
            return make_response(jsonify(data), 200)