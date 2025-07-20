from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.caracteristica_complementaria import Caracteristica_complementaria
from schemas.caracteristica_complementaria import caracteristica_complementaria_schema, caracteristicas_complementarias_schema

car_complementarias_routes = Blueprint('car_complementarias_routes', __name__)

@car_complementarias_routes.route("/get_car_complementarias", methods=["GET"])
def get_car_complementarias():
    caracteristicas = Caracteristica_complementaria.query.all()

    if not caracteristicas:
        data = {
            'message': 'No se encontraron caracteristicas complementarias.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = caracteristicas_complementarias_schema.dump(caracteristicas)
        data = {
            'message': 'Caracteristicas complementarias encontradas.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@car_complementarias_routes.route("/get_car_complementaria", methods=["POST"])
def get_car_complementaria():
    id_caracteristica = request.json.get('id_caracteristica')
    if not id_caracteristica:
        data = {
            'message': 'ID de caracteristica complementaria no proporcionado.',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    else:
        raza = Caracteristica_complementaria.query.get(id_caracteristica)

        if not raza:
            data = {
                'message': 'Caracteristica complementaria no encontrada.',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        else:
            result = caracteristica_complementaria_schema.dump(raza)
            data = {
                'message': 'Caracteristica complementaria encontrada.',
                'status': 200,
                'data': result
            }
            return make_response(jsonify(data), 200)