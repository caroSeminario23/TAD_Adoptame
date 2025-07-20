from flask import Blueprint, request, jsonify, make_response
import requests

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}

federador_routes = Blueprint("federador_routes", __name__)
@federador_routes.route("/buscar_tipo_mascota", methods=["POST"])
def route_buscar_tipo_mascota():
    payload = request.get_json() # incluye "id_tipo_mascota" y "origen"
    
    origen = payload.get("origen")
    id_tipo = payload.get("id_tipo_mascota")

    if not origen or not id_tipo:
        return make_response(jsonify({
            "message": "Datos incompletos",
            "status": 400
        }), 400)

    url = ALBERGUES.get(origen)

    if not url:
        return make_response(jsonify({
            "message": f"Origen '{origen}' no válido.",
            "status": 404
        }), 404)

    try:
        response = requests.post(f"{url}/tipo_mascota_routes/get_tipo_mascota", json={"id_tipo_mascota": id_tipo}, timeout=5)

        if response.status_code == 200:
            albergue_response = response.json()
            tipo_data = albergue_response.get("data")

            # Agregamos el origen al resultado
            if isinstance(tipo_data, dict):
                tipo_data["origen"] = origen

            return make_response(jsonify({
                "data": tipo_data,
                "message": "Tipo de mascota encontrado.",
                "status": 200
            }), 200)
        else:
            return make_response(jsonify({
                "message": "No se encontró el tipo de mascota.",
                "status": 404
            }), 404)

    except Exception as e:
        print(f"Error al conectar con {origen}: {e}")
        return make_response(jsonify({
            "message": f"No se pudo conectar con el origen {origen}.",
            "status": 500
        }), 500)