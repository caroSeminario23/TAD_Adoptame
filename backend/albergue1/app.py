from flask import Flask
from flask_cors import CORS
from utils.db import db
import os

from services.raza import raza_routes
from services.tipo_mascota import tipo_mascota_routes
from services.caracteristica_complementaria import car_complementarias_routes
from services.mascota import mascota_routes
from services.caracteristica_mascota import car_mascotas_routes

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app = Flask(__name__)

CORS(
    app, 
    origins = ['localhost'], #dirección del front-end
    methods = ['GET', 'POST'],
    allow_headers = ['Content-Type', 'Authorization']
)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db.init_app(app)

app.register_blueprint(raza_routes, url_prefix='/raza_routes')
app.register_blueprint(tipo_mascota_routes, url_prefix='/tipo_mascota_routes')
app.register_blueprint(car_complementarias_routes, url_prefix='/car_complementarias_routes')
app.register_blueprint(mascota_routes, url_prefix='/mascota_routes')
app.register_blueprint(car_mascotas_routes, url_prefix='/car_mascotas_routes')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port=port)