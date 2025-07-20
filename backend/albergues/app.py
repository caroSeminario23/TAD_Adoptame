from flask import Flask
from flask_cors import CORS
from utils.db import db
import os

from services.albergue import albergue_routes
from services.representante_albergue import representate_albergue_routes
from services.servicio import servicio_routes
from services.federacion.listar_car_complementarias import federador_routes as listar_car_complementarias_routes
from services.federacion.listar_car_mascotas import federador_routes as listar_car_mascotas_routes
from services.federacion.listar_mascotas import federador_routes as listar_mascotas_routes
from services.federacion.listar_razas import federador_routes as listar_razas_routes
from services.federacion.listar_tipo_mascotas import federador_routes as listar_tipo_mascotas_routes
from services.federacion.buscar_car_complementaria import federador_routes as buscar_car_complementaria_routes
from services.federacion.buscar_car_mascota import federador_routes as buscar_car_mascota_routes
from services.federacion.buscar_mascota import federador_routes as buscar_mascota_routes
from services.federacion.buscar_raza import federador_routes as buscar_raza_routes
from services.federacion.buscar_tipo_mascota import federador_routes as buscar_tipo_mascota_routes

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app = Flask(__name__)

CORS(
    app, 
    origins = ['localhost', 'http://localhost:4200'], #dirección del front-end
    methods = ['GET', 'POST'],
    allow_headers = ['Content-Type', 'Authorization']
)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db.init_app(app)

app.register_blueprint(albergue_routes, url_prefix='/albergue_routes')
app.register_blueprint(representate_albergue_routes, url_prefix='/representante_routes')
app.register_blueprint(servicio_routes, url_prefix='/servicio_routes')
app.register_blueprint(listar_car_complementarias_routes, url_prefix='/federador_routes', name='listar_car_complementarias')
app.register_blueprint(listar_car_mascotas_routes, url_prefix='/federador_routes', name='listar_car_mascotas')
app.register_blueprint(listar_mascotas_routes, url_prefix='/federador_routes', name='listar_mascotas')
app.register_blueprint(listar_razas_routes, url_prefix='/federador_routes', name='listar_razas')
app.register_blueprint(listar_tipo_mascotas_routes, url_prefix='/federador_routes', name='listar_tipo_mascotas')
app.register_blueprint(buscar_car_complementaria_routes, url_prefix='/federador_routes', name='buscar_car_complementaria')
app.register_blueprint(buscar_car_mascota_routes, url_prefix='/federador_routes', name='buscar_car_mascota')
app.register_blueprint(buscar_mascota_routes, url_prefix='/federador_routes', name='buscar_mascota')
app.register_blueprint(buscar_raza_routes, url_prefix='/federador_routes', name='buscar_raza')
app.register_blueprint(buscar_tipo_mascota_routes, url_prefix='/federador_routes', name='buscar_tipo_mascota')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', debug=True, port=port)