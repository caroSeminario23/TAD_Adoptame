from flask import Blueprint, request, jsonify, make_response
import requests



ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}

federado_routes = Blueprint("federado_routes", __name__)
@federado_routes.route("/buscar_caracteristica_complementaria", methods=["POST"])

def route_buscar_car_complementaria():
    payload = request.get_json('id_caracteristica')
    if not payload:
        return make_response(jsonify({
            "message": "Payload no proporcionado.",
            "status": 400
        }), 400)

    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.post(f"{base_url}/car_complementarias_routes/get_car_complementaria", json=payload, timeout=5)
            if response.status_code == 200:
                json_data = response.json().get("data", [])
                for item in json_data:
                    item["origen"] = nombre
                resultados.extend(json_data)
        except Exception:
            continue

    if not resultados:
        return make_response(jsonify({
            "message": "Característica complementaria no encontrada.",
            "status": 404
        }), 404)
    else:
        return make_response(jsonify({
            "message": "Característica complementaria encontrada.",
            "status": 200,
            "data": resultados
        }), 200)
