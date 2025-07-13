from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.caracteristica_mascota import Caracteristica_mascota
from schemas.caracteristica_mascota import caracteristicas_mascotas_schema, caracteristica_mascota_schema

car_mascotas_routes = Blueprint('car_mascotas_routes', __name__)

@car_mascotas_routes.route("/get_car_mascotas", methods=["GET"])
def get_car_complementarias():
    caracteristicas = Caracteristica_mascota.query.all()

    if not caracteristicas:
        data = {
            'message': 'No se encontraron caracteristicas de mascota.',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    else:
        result = caracteristicas_mascotas_schema.dump(caracteristicas)
        data = {
            'message': 'Caracteristicas de mascota encontradas.',
            'status': 200,
            'data': result
        }
        return make_response(jsonify(data), 200)
    
@car_mascotas_routes.route("/get_car_mascota", methods=["POST"])
def get_car_complementaria():
    id_caracteristica = request.json.get('id_caracteristica')
    if not id_caracteristica:
        data = {
            'message': 'ID de caracteristica de mascota no proporcionado.',
            'status': 400
        }
        return make_response(jsonify(data), 400)
    else:
        raza = Caracteristica_mascota.query.get(id_caracteristica)

        if not raza:
            data = {
                'message': 'Caracteristica de mascota no encontrada.',
                'status': 404
            }
            return make_response(jsonify(data), 404)
        else:
            result = caracteristica_mascota_schema.dump(raza)
            data = {
                'message': 'Caracteristica de mascota encontrada.',
                'status': 200,
                'data': result
            }
            return make_response(jsonify(data), 200)