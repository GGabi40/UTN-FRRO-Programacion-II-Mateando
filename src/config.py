""" import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
 """

class Config():
    SECRET_KEY='1234'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///mateando.db'
    SQLALCHEMY_TRACK_MODIFITIATIONS = False