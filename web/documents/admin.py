from django.contrib import admin
from documents.models import Document, ArtBoard, Revision

admin.site.register(Document)
admin.site.register(ArtBoard)
admin.site.register(Revision)