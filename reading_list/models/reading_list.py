from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import PositiveSmallIntegerField
from django.db.models import UUIDField

from reading_list.models import User, Book


class ReadingList(Model):
    id = UUIDField(primary_key=True)
    user_id = ForeignKey(User, on_delete=CASCADE)
    book_id = ForeignKey(Book, on_delete=CASCADE)
    completed = BooleanField(default=False)
    progress = PositiveSmallIntegerField(default=0)
