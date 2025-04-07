from django.db import models
from .turma import Turma

class Semestre(models.Model):
    id = models.AutoField(primary_key=True) # Explicitly define auto-incrementing primary key
    semestre = models.IntegerField(unique=True) # Assuming semester number should be unique
    turmas = models.ManyToManyField(Turma, blank=True) # Allows a semestre to exist without turmas initially

    def __str__(self):
        return f"Semestre {self.semestre}"
