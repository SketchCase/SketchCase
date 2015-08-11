import time

from base64 import decodestring

from sketchcase.utils import crud
from sketchcase.handlers import JsonHandler
from sketchcase.schemas import revision_schema, document_schema, artboard_scehma


class RevisionList(JsonHandler):
    def get(self, artboard_id):
        self.response['data'] = crud.index_retrieve(
            'revisions', artboard_id, 'artboard_id')
        self.write_json()


class RevisionCreate(JsonHandler):
    """ RevisionList

    Currently only deals with the creation of revisions. If specified
    document or artboard does not exist, it is automatically created.
    """
    def post(self):
        data = self.request.arguments
        filepath = self.save_image(data)
        document = self.retrieve_or_create_document(data)
        artboard = self.retrieve_or_create_artboard(data, document)

        revision = {
            'artboard_id': artboard['id'],
            'image_url': filepath
        }

        self.response['data'] = crud.create(
            'revisions', revision, revision_schema)
        self.write_json()

    def save_image(self, data):
        filepath = '/media/%s_%s_%d.png' % (
            data['document'],
            data['artboard'],
            int(time.time()))
        filepath = filepath.replace(' ', '_')  # replace spaces with underscores

        with open(filepath, 'w') as f:
            f.write(decodestring(data['image']))

        return filepath

    def retrieve_or_create_document(self, data):
        return crud.retrieve_create(
            'documents',
            data['document'],
            'name',
            {'name': data['document']},
            document_schema)

    def retrieve_or_create_artboard(self, data, document):
        return crud.retrieve_create(
            'artboards',
            [data['artboard'], document['id']],
            'name_and_document',
            {'name': data['artboard'], 'document_id': document['id']},
            artboard_scehma)
