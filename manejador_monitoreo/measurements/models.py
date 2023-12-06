from django.db import models
from variables.models import Variable

class Measurement(models.Model):
    # ID automático de la medición
    id = models.AutoField(primary_key=True)

    # Valor de la medida
    value = models.DecimalField(max_digits=5, decimal_places=2)

    # Fecha y hora de la medida
    timestamp = models.DateTimeField(auto_now_add=True)

    # Relación muchos a uno con Variable
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)

    def __str__(self):
        return f'Medida ID: {self.id}, Valor: {self.value}, Fecha y Hora: {self.timestamp}'
