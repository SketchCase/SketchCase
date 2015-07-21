
import flask.ext.mongoengine

from flask import Blueprint, jsonify, request, Response
from sketchcase.models import SketchDocument, ArtBoard
from sketchcase.helpers import prep_doc_for_json

api = Blueprint('api/v1', __name__)

@api.route('/')
def api_root():
    return jsonify(documentation = [
        '/documents',
        '/documents/<id>'
    ])

# Document endpoints

@api.route('/documents', methods=['GET', 'POST'])
def documents():
    # List documents
    if request.method == 'GET':
        docs = [prep_doc_for_json(doc) for doc in SketchDocument.objects]
        return jsonify(data = docs)

    # Create document
    elif request.method == 'POST':
        doc = prep_doc_for_json(
            SketchDocument(**request.json).save())
        return jsonify(data = doc)

    return '', 500

@api.route('/documents/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def detail_document(id):
    # Retrieve document
    if request.method == 'GET':
        doc = prep_doc_for_json(SketchDocument.objects.get_or_404(id=id))
        return jsonify(data = doc)

    # Delete document
    elif request.method == 'DELETE':
        SketchDocument.objects.get_or_404(id=id).delete()
        return '', 204

    # Update document
    elif request.method == 'PUT':
        doc = SketchDocument.objects.get_or_404(id=id)
        if doc.modify(**request.json):
            return jsonify(data = prep_doc_for_json(doc))

    return '', 500

# Art board endpoints

@api.route('/documents/<string:did>/artboards', methods=['GET', 'POST'])
def artboards(did):
    # List art boards
    if request.method == 'GET':
        art_boards = ArtBoard.objects(sketch_document=did)
        docs = [prep_doc_for_json(doc, unicodify=['sketch_document']) for doc in art_boards]
        return jsonify(data = docs)

    # Create art board
    elif request.method == 'POST':
        ab = ArtBoard(**request.json)
        ab.sketch_document = SketchDocument(id=did)
        doc =  prep_doc_for_json(ab.save(), unicodify=['sketch_document'])
        return jsonify(data = doc)
