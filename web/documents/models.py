from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    owner = models.ForeignKey(User, related_name='documents')
    name = models.CharField(max_length=255)


class ArtBoard(models.Model):
    document = models.ForeignKey(Document, related_name='art_boards')
    name = models.CharField(max_length=255)


class Revision(models.Model):
    art_board = models.ForeignKey(ArtBoard, related_name='revisions')
    uploaded = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='revisions')