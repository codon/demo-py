from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import PositiveIntegerField
from django.db.models import SET_NULL
from django.db.models import TextField
from django.db.models import UUIDField

from reading_list.models import User, Book


class BookReview(Model):
    id = UUIDField(primary_key=True)
    user_id = ForeignKey(User, null=True, on_delete=SET_NULL)
    book_id = ForeignKey(Book, null=True, on_delete=SET_NULL)
    rating = PositiveIntegerField()
    review = TextField(null=True)