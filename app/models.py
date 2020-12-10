from django.db import models
from django.db.models import CharField
from django.db.models import JSONField


class DataFields(models.Model):
	name = CharField(max_length=200)
	about_me = JSONField(default=dict)
