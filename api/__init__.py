from flask import Flask, jsonify
from api.animals.endpoints import animal
from mongoengine import connect
import settings
from api.authentication.auth_error import AuthError

connect(host=settings.MONGODB_URI)
app = Flask(__name__) 

app.register_blueprint(animal)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
