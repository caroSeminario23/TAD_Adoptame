from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.representante_albergue import Representante_albergue
from schemas.representante_albergue import representantes_albergues_schema, representante_albergue_schema

representate_albergue_routes = Blueprint('representante_routes', __name__)

@representate_albergue_routes.route("/get_representantes_albergues", methods=["GET"])
def get_representantes_albergues():
    representantes_albergues = Representante_albergue.query.all()

    if not representantes_albergues:
        data = {
            'message': 'No se encontraron representantes de albergues.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = representantes_albergues_schema.dump(representantes_albergues)
        data = {
            'message': 'Representantes de albergues encontrados.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@representate_albergue_routes.route("/get_representante_albergue/<int:id_representante>", methods=["GET"])
def get_representante_albergue(id_representante):
    representante_albergue = Representante_albergue.query.get(id_representante)

    if not representante_albergue:
        data = {
            'message': 'Representante de albergue no encontrado.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = representante_albergue_schema.dump(representante_albergue)
        data = {
            'message': 'Representante de albergue encontrado.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)