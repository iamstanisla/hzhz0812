from django.db import models
from django.db.models import CharField
from django.db.models import JSONField


class User(models.Model):
	data_fields = JSONField(default=dict)
