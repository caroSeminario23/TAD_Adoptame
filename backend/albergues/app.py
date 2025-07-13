from flask import Flask
from flask_cors import CORS
from utils.db import db
import os

from services.albergue import albergue_routes
from services.representante_albergue import representate_albergue_routes
from services.servicio import servicio_routes

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

app.register_blueprint(albergue_routes, url_prefix='/albergue_routes')
app.register_blueprint(representate_albergue_routes, url_prefix='/representante_routes')
app.register_blueprint(servicio_routes, url_prefix='/servicio_routes')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port=port)