from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import Model
from django.db.models import UUIDField


class User(Model):
    id = UUIDField(primary_key=True)
    username = CharField(max_length=125, unique=True, db_index=True)
    password = CharField(max_length=255)
    last_login_at = DateTimeField()
    created_at = DateTimeField()
