from mongoengine import StringField, EmbeddedDocument, ListField, EmbeddedDocumentField, ReferenceField, FileField, CASCADE
from flask.ext.mongoengine import Document


class SketchDocument(Document):
    """ Model for the actual Sketch document
    """
    name = StringField(required=True)


class Revision(EmbeddedDocument):
    """ Model for revisions of an art board. Each new upload creates a new
    revision instead of overwriting the current one.
    """
    image = FileField()


class ArtBoard(Document):
    """

    """
    sketch_document = ReferenceField(SketchDocument)
    name = StringField(required=True)
    revisions = ListField(EmbeddedDocumentField(Revision))

# Makes sure to delete art boards belonging to a document on document deletion
ArtBoard.register_delete_rule(SketchDocument, 'artboard', CASCADE)
