from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.raza import Raza
from schemas.raza import raza_schema, razas_schema

raza_routes = Blueprint('raza_routes', __name__)

@raza_routes.route("/get_razas", methods=["GET"])
def get_razas():
    razas = Raza.query.all()

    if not razas:
        data = {
            'message': 'No se encontraron razas.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = razas_schema.dump(razas)
        data = {
            'message': 'Razas encontradas.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@raza_routes.route("/get_raza", methods=["POST"])
def get_raza():
    id_raza = request.json.get('id_raza')
    if not id_raza:
        data = {
            'message': 'ID de raza no proporcionado.',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    else:
        raza = Raza.query.get(id_raza)

        if not raza:
            data = {
                'message': 'Raza no encontrada.',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        else:
            result = raza_schema.dump(raza)
            data = {
                'message': 'Raza encontrada.',
                'status': 200,
                'data': result
            }
            return make_response(jsonify(data), 200)