from flask import Flask
from flask_cors import CORS
from flask_mongoalchemy import MongoAlchemy
from config import Config
import os
UPLOAD_FOLDER='/uploads'
db = MongoAlchemy()
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config.from_object(Config)
    db.init_app(app)
    return app

