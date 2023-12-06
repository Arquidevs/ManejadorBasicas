from django.db import models

###Tabla Servicio
class Servicio(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    tipo = models.CharField(max_length=40, choices=[('Radiografia', 'radiografia'), 
                                                       ('Tomografia', 'tomografia'),
                                                       ('Examen de Sangre', 'examen de sangre'),
                                                       ('Ecografia', 'ecografia'),
                                                       ('Cita Medica', 'cita medica')])
    descripcion = models.TextField()
