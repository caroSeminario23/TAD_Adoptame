from flask import Blueprint, request, jsonify, make_response
import requests



ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}

federador_routes = Blueprint("federador_routes", __name__)
@federador_routes.route("/buscar_mascota", methods=["POST"])
def route_buscar_mascota():
    payload = request.get_json('id_mascota')
    if not payload:
        return make_response(jsonify({
            "message": "Payload no proporcionado.",
            "status": 400
        }), 400)

    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.post(f"{base_url}/mascota_routes/get_mascota", json=payload, timeout=5)
            if response.status_code == 200:
                json_data = response.json().get("data", [])
                # Agregar origen a cada elemento individual
                for item in json_data:
                    item_con_origen = item.copy()
                    item_con_origen["origen"] = nombre
                    resultados.append(item_con_origen)
        except Exception:
            continue

    if not resultados:
        return make_response(jsonify({
            "message": "Mascota no encontrada.",
            "status": 404
        }), 404)
    else:
        return make_response(jsonify({
            "message": "Mascota encontrada.",
            "status": 200,
            "data": resultados
        }), 200)