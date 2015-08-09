from sketchcase.utils import crud
from sketchcase.handlers import JsonHandler
from sketchcase.schemas import document_schema


class DocumentList(JsonHandler):
    def get(self):
        self.response['data'] = crud.list('documents')
        self.write_json()

    def post(self):
        self.response['data'] = crud.create(
            'documents', self.request.arguments, document_schema)
        self.set_status(201)
        self.write_json()


class DocumentDetail(JsonHandler):
    def get(self, id):
        self.response['data'] = crud.retrieve('documents', id)
        self.write_json()

    def delete(self, id):
        crud.delete('documents', id)
        self.write_empty()

    def put(self, id):
        self.response['data'] = crud.update(
            'documents', id, self.request.arguments, document_schema)
        self.write_json()
