"""
Módulo inicializador da aplicação de API
"""
from flask import Flask
from mongoengine import connect
from api.animals.endpoints import ANIMAL
import settings
from api.authentication.auth_error import AuthError

connect(host=settings.MONGODB_URI)
APP = Flask(__name__)

APP.register_blueprint(ANIMAL)
