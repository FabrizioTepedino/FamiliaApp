from django.db import models

# Create your models here.

class Familia(models.Model):

    relacion = models.CharField('relacion', max_length=50)
    nombre = models.CharField('nombre', max_length=50)
    edad = models.CharField('edad', max_length=50)
    cumpleagnos = models.CharField('cumpleagnos', max_length=8)