from django.db import models

###Tabla Contrato
class Contrato(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    eps = models.CharField(max_length=50)
    descripcion = models.TextField()