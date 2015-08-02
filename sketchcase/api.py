import time
from base64 import decodestring

from flask import Blueprint, jsonify, request

from sketchcase.schemas import document_schema, artboard_scehma, revision_schema
from sketchcase.auth import actions as user_actions
from sketchcase import crud

api = Blueprint('api/v1', __name__)


@api.route('/')
def api_root():
    return jsonify(documentation=[
        '/documents',
        '/documents/<document-id>',
        '/documents/<document-id>/artboards',
        '/documents/<document-id>/artboards/<artboard-id>',
        '/documents/<document-id>/artboards/<artboard-id>/revisions',
        '/revisions'
    ])


# User/Auth
@api.route('/auth', methods=['POST'])
def auth():
    # Authorize user
    return jsonify(data=user_actions.retrieve_token(request.json))


# Document endpoints
@api.route('/documents', methods=['GET', 'POST'])
def documents():
    # List documents
    if request.method == 'GET':
        return jsonify(data=crud.list('documents'))

    # Create document
    elif request.method == 'POST':
        response = jsonify(data=crud.create(
            'documents', request.json, document_schema))
        response.status_code = 201
        return response

    return '', 500


@api.route('/documents/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def detail_document(id):
    # Retrieve document
    if request.method == 'GET':
        return jsonify(data=crud.retrieve('documents', id))

    # Delete document
    elif request.method == 'DELETE':
        crud.delete('documents', id)
        return '', 204

    # Update document
    elif request.method == 'PUT':
        return jsonify(data=crud.update(
            'documents', id, request.json, document_schema))

    return '', 500


# Art board endpoints
@api.route('/documents/<string:did>/artboards', methods=['GET', 'POST'])
def artboards(did):
    # List art boards
    if request.method == 'GET':
        return jsonify(data=crud.list('artboards'))

    # Create art board
    elif request.method == 'POST':
        data = request.json
        data['document_id'] = did
        return jsonify(data=crud.create('artboards', data, artboard_scehma))

    return '', 500


@api.route('/documents/<string:did>/artboards/<string:aid>',
           methods=['GET', 'DELETE', 'PUT'])
def detail_artboard(did, aid):
    # Retrieve art board
    if request.method == 'GET':
        return jsonify(data=crud.retrieve('artboards', aid))

    # Delete art board
    elif request.method == 'DELETE':
        crud.delete('artboards', aid)
        return '', 204

    # Update art board
    elif request.method == 'PUT':
        return jsonify(data=crud.update(
            'artboards', aid, request.json, artboard_scehma))

    return '', 500


# Revisions
@api.route('/documents/<string:did>/artboards/<string:aid>/revisions',
           methods=['GET'])
def revisions(did, aid):
    if request.method == 'GET':
        return jsonify(data=crud.index_retrieve(
            'revisions', aid, 'artboard_id'))

    return '', 500


@api.route('/revisions', methods=['POST'])
def detail_revision():
    data = request.json
    filepath = 'media/%s_%s_%d.png' % (
        data['document'],
        data['artboard'],
        int(time.time()))

    with open(filepath, 'w') as f:
        f.write(decodestring(data['image']))

    document = crud.retrieve_create(
        'documents',
        data['document'],
        'name',
        {'name': data['document']},
        document_schema)

    artboard = crud.retrieve_create(
        'artboards',
        [data['artboard'], document['id']],
        'name_and_document',
        {'name': data['artboard'], 'document_id': document['id']},
        artboard_scehma)

    revision = {
        'artboard_id': artboard['id'],
        'image_url': filepath
    }

    return jsonify(data=crud.create(
        'revisions', revision, revision_schema))
