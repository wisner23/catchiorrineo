from flask import Flask, jsonify
from mongoengine import connect
import settings
from api.animals.endpoints import ANIMAL
from .common.exceptions import InvalidInput, AuthError

connect(host=settings.MONGODB_URI)


def handle_invalid_input(error):
    """Trata exceções do tipo InvalidInput,
    retornando o dicionário de mensagens e
    o status 400 BAD REQUEST"""
    response = jsonify(error.errors)
    response.status_code = error.status_code
    return response


def handle_invalid_authorization(exception):
    """Trata exceções do tipo InvalidInput,
    retornando o dicionário de mensagens e
    o status 401 Unauthorized"""
    response = jsonify(exception.error)
    response.status_code = exception.status_code
    return response


def create_app():
    app = Flask(__name__)
    app.register_blueprint(ANIMAL)
    register_exceptions(app)
    return app


def register_exceptions(app):
    app.register_error_handler(InvalidInput, handle_invalid_input)
    app.register_error_handler(AuthError, handle_invalid_authorization)
