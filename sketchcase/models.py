from mongoengine import StringField, EmbeddedDocument, ListField, EmbeddedDocumentField, ReferenceField, CASCADE
from flask.ext.mongoengine import Document


class SketchDocument(Document):
    name = StringField(required=True)


class Revision(EmbeddedDocument):
    image_path = StringField()


class ArtBoard(Document):
    sketch_document = ReferenceField(SketchDocument)
    name = StringField(required=True)
    revisions = ListField(EmbeddedDocumentField(Revision))

ArtBoard.register_delete_rule(SketchDocument, 'artboard', CASCADE)
