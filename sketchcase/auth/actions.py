from jsonschema import validate

from sketchcase.auth.schemas import user_schema


def retrieve_token(data):
    validate(data, user_schema)
