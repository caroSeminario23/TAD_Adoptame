from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.albergue import Albergue
from schemas.albergue import albergues_schema, albergue_schema

albergue_routes = Blueprint('albergue_routes', __name__)

@albergue_routes.route("/get_albergues", methods=["GET"])
def get_albergues():
    albergues = Albergue.query.all()

    if not albergues:
        data = {
            'message': 'No se encontraron albergues.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = albergues_schema.dump(albergues)
        data = {
            'message': 'Albergues encontrados.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@albergue_routes.route("/get_albergue", methods=["POST"])
def get_albergue():
    id_albergue = request.json.get('id_albergue')
    if not id_albergue:
        data = {
            'message': 'ID de albergue no proporcionado.',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    else:
        albergue = Albergue.query.get(id_albergue)

        if not albergue:
            data = {
                'message': 'Albergue no encontrado.',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        else:
            result = albergue_schema.dump(albergue)
            data = {
                'message': 'Albergue encontrado.',
                'status': 200,
                'data': result
            }
            return make_response(jsonify(data), 200)