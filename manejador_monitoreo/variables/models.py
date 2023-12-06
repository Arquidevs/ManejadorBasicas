from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.name