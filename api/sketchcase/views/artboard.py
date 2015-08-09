from sketchcase.utils import crud
from sketchcase.handlers import JsonHandler
from sketchcase.schemas import artboard_scehma


class ArtboardList(JsonHandler):
    def get(self, document_id):
        self.response['data'] = crud.list('artboards')
        self.write_json()

    def post(self, document_id):
        data = self.request.arguments
        data['document_id'] = document_id

        self.response['data'] = crud.create(
            'artboards', data, artboard_scehma)


class ArtboardDetail(JsonHandler):
    def get(self, id):
        self.response['data'] = crud.retrieve('artboards', id)
        self.write_json()

    def delete(self, id):
        crud.delete('artboards', id)
        self.write_empty()

    def put(self, id):
        self.response['data'] = crud.update(
            'artboards', id, self.request.arguments, artboard_scehma)
        self.write_json()
