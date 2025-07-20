from flask import Blueprint, request, jsonify, make_response
import requests


ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}

federador_routes = Blueprint("federador_routes", __name__)
@federador_routes.route("/listar_car_complementarias", methods=["GET"])
def listar_car_complementarias():
    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.get(f"{base_url}/car_complementarias_routes/get_car_complementarias", timeout=5)
            if response.status_code == 200:
                json_data = response.json().get("data", [])
                resultados.extend(json_data)
        except Exception:
            continue

    if not resultados:
        return make_response(jsonify({
            "message": "No se encontraron características complementarias.",
            "status": 404
        }), 404)
    else:
        return make_response(jsonify({
            "message": "Características complementarias encontradas.",
            "status": 200,
            "data": resultados
        }), 200)