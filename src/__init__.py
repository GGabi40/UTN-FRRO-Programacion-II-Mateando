from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def crear_app() -> Flask:
    app = Flask(__name__, template_folder="../templates")
    app.config.from_object(obj=Config)
    
    db.init_app(app)
    
    return app