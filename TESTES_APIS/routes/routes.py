from flask import Blueprint, Flask
from routes.funct_cliente import cliente_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(cliente_bp)
    return app