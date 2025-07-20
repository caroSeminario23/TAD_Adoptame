from flask import Blueprint, request, jsonify, make_response
import requests

federado_routes = Blueprint("federado_routes", __name__)

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}
@federado_routes.route("/federado/caracteristica_complementaria/listar", methods=["GET"])
def route_listar_car_complementarias():
    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.get(f"{base_url}/car_complementarias_routes/get_car_complementarias", timeout=5)
            if response.status_code == 200:
                resultados.append({"origen": nombre, "data": response.json()})
        except Exception as e:
            resultados.append({"origen": nombre, "error": str(e)})

    if not resultados:
        return make_response(jsonify({"message": "No se encontraron características complementarias.", "status": 404}), 404)
    else:
        return make_response(jsonify({"message": "Características complementarias encontradas.", "status": 200, "data": resultados}), 200)