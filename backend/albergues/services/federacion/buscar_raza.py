from flask import Blueprint, request, jsonify, make_response
import requests

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}

federador_routes = Blueprint("federador_routes", __name__)
@federador_routes.route("/buscar_raza", methods=["POST"])
def route_buscar_raza():
    payload = request.get_json() # incluye "id_raza" y "origen"

    origen = payload.get("origen")
    id_raza = payload.get("id_raza")

    if not origen or not id_raza:
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
        response = requests.post(f"{url}/raza_routes/get_raza", json={"id_raza": id_raza}, timeout=5)

        if response.status_code == 200:
            albergue_response = response.json()
            raza_data = albergue_response.get("data")

            # Agregamos el origen al resultado
            if isinstance(raza_data, dict):
                raza_data["origen"] = origen

            return make_response(jsonify({
                "data": raza_data,
                "message": "Raza encontrada.",
                "status": 200
            }), 200)
        else:
            return make_response(jsonify({
                "message": "No se encontró la raza.",
                "status": 404
            }), 404)
    except Exception as e:
        print(f"Error al conectar con {origen}: {e}")
        return make_response(jsonify({
            "message": f"No se pudo conectar con el origen {origen}.",
            "status": 500
        }), 500)