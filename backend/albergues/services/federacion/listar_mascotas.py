from flask import Blueprint, request, jsonify, make_response
import requests

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}

federador_routes = Blueprint("federador_routes", __name__)
@federador_routes.route("/listar_mascotas", methods=["GET"])
def route_listar_mascotas():
    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.get(f"{base_url}/mascota_routes/get_mascotas", timeout=5)
            if response.status_code == 200:
                json_data = response.json().get("data", [])
                for item in json_data:
                    item["origen"] = nombre
                    resultados.append(item)
                #resultados.extend(json_data)
        except Exception as e:
            print(f"Error al conectar con {nombre}: {e}")
            continue

    if not resultados:
        return make_response(jsonify({
            "message": "No se encontraron mascotas.",
            "status": 404
        }), 404)
    else:
        return make_response(jsonify({
            "message": "Mascotas encontradas.",
            "status": 200,
            "data": resultados
        }), 200)