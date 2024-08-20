from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(main)
    app.debug = True  # Habilita el modo de depuración
    return app
