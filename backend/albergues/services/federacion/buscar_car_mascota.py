import requests
from flask import jsonify, make_response

ALBERGUES = {
    "albergue1": "http://127.0.0.1:5000",
    "albergue2": "http://127.0.0.1:8080",
    "albergue3": "http://127.0.0.1:3000"
}
def buscar_car_mascota(payload):
    resultados = []
    for nombre, base_url in ALBERGUES.items():
        try:
            response = requests.post(f"{base_url}/car_mascotas_routes/get_car_mascota", json=payload, timeout=5)
            if response.status_code == 200:
                resultados.append({"origen": nombre, "data": response.json()})
        except Exception as e:
            resultados.append({"origen": nombre, "error": str(e)})

    if not resultados:
        return make_response(jsonify({
            "message": "Característica de mascota no encontrada.",
            "status": 404
        }), 404)
    else:
        return make_response(jsonify({
            "message": "Característica de mascota encontrada.",
            "status": 200,
            "data": resultados
        }), 200)