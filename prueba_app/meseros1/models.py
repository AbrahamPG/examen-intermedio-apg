from django.db import models


# Create your models here.
class Meseros1(models.Model):
    nombre = models.CharField(max_length=25)
    nacionalidad = models.CharField(max_length=25)
    edad = models.IntegerField()
