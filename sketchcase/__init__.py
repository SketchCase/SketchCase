from flask import Flask, jsonify
from jsonschema.exceptions import ValidationError
from sketchcase.api import api

app = Flask(__name__)
app.config.from_envvar('SKETCHCASE_SETTINGS')


@app.errorhandler(405)
def not_allowed(error):
    response = jsonify(errors=['Method not allowed'])
    response.status_code = 405
    return response


@app.errorhandler(404)
def not_found(error):
    response = jsonify(errors=['Not found'])
    response.status_code = 404
    return response


@app.errorhandler(ValidationError)
def validation_error(error):
    response = jsonify(errors=[error.message])
    response.status_code = 400
    return response

app.register_blueprint(api, url_prefix='/api/v1')
