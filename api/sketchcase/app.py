import tornado.web

from sketchcase.views.document import DocumentList, DocumentDetail
from sketchcase.views.artboard import ArtboardList, ArtboardDetail


def make_app():
    return tornado.web.Application([
        (r'/api/v1/documents', DocumentList),
        (r'/api/v1/documents/([\w-]+)', DocumentDetail),
        (r'/api/v1/documents/([\w-]+)/artboards', ArtboardList),
        (r'/api/v1/artboards/([\w-]+)', ArtboardDetail)
    ], debug=True)


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
