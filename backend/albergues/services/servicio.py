from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.servicio import Servicio
from schemas.servicio import servicios_schema, servicio_schema

servicio_routes = Blueprint('servicio', __name__)

@servicio_routes.routes("/get_servicios", methods=["GET"])
def get_servicios():
    albergues = Servicio.query.all()

    if not albergues:
        data = {
            'message': 'No se encontraron servicios.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = servicios_schema.dump(albergues)
        data = {
            'message': 'Servicios encontrados.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@servicio_routes.route("/get_servicio/<int:id_servicio>", methods=["GET"])
def get_servicio(id_servicio):
    servicio = Servicio.query.get(id_servicio)

    if not servicio:
        data = {
            'message': 'Servicio no encontrado.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = servicio_schema.dump(servicio)
        data = {
            'message': 'Servicio encontrado.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)