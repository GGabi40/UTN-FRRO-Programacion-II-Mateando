import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    if not SQLALCHEMY_DATABASE_URI:
            raise ValueError("DATABASE_URL no está definida. Verifica las variables de entorno.")
