from flask import Flask, jsonify
from flask.ext.mongoengine import MongoEngine
from sketchcase.api import api

app = Flask(__name__)
app.config.from_envvar('SKETCHCASE_SETTINGS')
db = MongoEngine(app)

@app.errorhandler(405)
def not_allowed(error):
    response = jsonify(error = 'Method not allowed')
    response.status_code = 405
    return response

@app.errorhandler(404)
def not_allowed(error):
    response = jsonify(error = 'Not found')
    response.status_code = 404
    return response

app.register_blueprint(api, url_prefix='/api/v1')
