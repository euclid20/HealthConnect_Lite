import os 

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.config.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode= None):
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    app = Flask(__name__, template_folder=template_path)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
