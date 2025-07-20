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
    payload = request.get_json('id_raza')
    if not payload:
        return make_response(jsonify({"message": "Payload no proporcionado.", "status": 400}), 400)

    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.post(f"{base_url}/raza_routes/get_raza", json=payload, timeout=5)
            if response.status_code == 200:
                resultados.append({"origen": nombre, "data": response.json()})
        except Exception as e:
            resultados.append({"origen": nombre, "error": str(e)})

    if not resultados:
        return make_response(jsonify({
            "message": "Raza no encontrada.",
            "status": 404
        }), 404)
    else:
        return make_response(jsonify({
            "message": "Raza encontrada.",
            "status": 200,
            "data": resultados
        }), 200)