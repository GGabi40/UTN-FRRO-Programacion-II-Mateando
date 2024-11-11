from dotenv import load_dotenv
load_dotenv()

import os

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///mateando.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    
    SQLALCHEMY_TRACK_MODIFITIATIONS = False