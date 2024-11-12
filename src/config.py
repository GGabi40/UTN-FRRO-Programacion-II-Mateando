import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "1234")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///mateando.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
