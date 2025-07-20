import requests
from flask import jsonify, make_response

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}
def listar_mascotas():
    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.get(f"{base_url}/mascota_routes/get_mascotas", timeout=5)
            if response.status_code == 200:
                resultados.append({"origen": nombre, "data": response.json()})
        except Exception as e:
            resultados.append({"origen": nombre, "error": str(e)})

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