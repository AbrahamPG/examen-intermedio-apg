from django.db import models


# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=25)
    procedencia = models.CharField(max_length=25, default='')
    precio = models.FloatField()
