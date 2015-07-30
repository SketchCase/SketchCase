from flask import Blueprint, jsonify, request
from sketchcase.schemas import document_schema, artboard_scehma
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
           methods=['POST'])
def revisions(did, aid):
    if request.method == 'GET':
        return jsonify(data=crud.list('revisions'))

    return '', 500
