import tornado.web

from sketchcase.views.document import DocumentList, DocumentDetail
from sketchcase.views.artboard import ArtboardList, ArtboardDetail
from sketchcase.views.revision import RevisionList, RevisionCreate


def make_app():
    return tornado.web.Application([
        (r'/api/v1/documents', DocumentList),
        (r'/api/v1/documents/([\w-]+)', DocumentDetail),
        (r'/api/v1/documents/([\w-]+)/artboards', ArtboardList),
        (r'/api/v1/artboards/([\w-]+)', ArtboardDetail),
        (r'/api/v1/artboards/([\w-]+)/revisions', RevisionList),
        (r'/api/v1/revisions', RevisionCreate)
    ], debug=True)


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
