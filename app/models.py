from django.db import models

# Create your models here.


class DataFields(models.Model):
	one_filed = models.CharField(max_length=200)
