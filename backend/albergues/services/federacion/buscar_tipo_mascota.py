from flask import Blueprint, request, jsonify, make_response
import requests

federado_routes = Blueprint("federado_routes", __name__)

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}
@federado_routes.route("/federado/tipo_mascota/buscar", methods=["POST"])
def route_buscar_tipo_mascota():
    payload = request.get_json()
    if not payload:
        return make_response(jsonify({"message": "Payload no proporcionado.", "status": 400}), 400)

    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.post(f"{base_url}/tipo_mascota_routes/get_tipo_mascota", json=payload, timeout=5)
            if response.status_code == 200:
                resultados.append({"origen": nombre, "data": response.json()})
        except Exception as e:
            resultados.append({"origen": nombre, "error": str(e)})

    if not resultados:
        return make_response(jsonify({"message": "Tipo de mascota no encontrado.", "status": 404}), 404)
    else:
        return make_response(jsonify({"message": "Tipo de mascota encontrado.", "status": 200, "data": resultados}), 200)