from django.db import models

# Create your models here.


class Number(models.Model):
    number: models.CharField = models.CharField(max_length=200)
