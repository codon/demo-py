from django.db.models import CharField
from django.db.models import DateField
from django.db.models import Model
from django.db.models import TextField
from django.db.models import UUIDField


class Book(Model):
    id = UUIDField(primary_key=True)
    title = TextField()
    author = CharField(max_length=255)
    isbn = CharField(max_length=128)
    publication_date = DateField()
