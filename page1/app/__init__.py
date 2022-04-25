from flask import Flask

#importacion de BLueprint
from .admin import admin

def create_app():
    app = Flask(__name__)

    app.register_blueprint(admin)
    
    return app
    