from django.db import models
from .turma import Turma
from .campus import Campus

class Semestre(models.Model):
    id = models.AutoField(primary_key=True) # Explicitly define auto-incrementing primary key
    semestre = models.IntegerField()
    TURNO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
    ]
    turno = models.CharField(max_length=5, choices=TURNO_CHOICES, default='MANHA')
    tag = models.CharField(max_length=3)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    turmas = models.ManyToManyField(Turma, blank=True) # Allows a semestre to exist without turmas initially

    def __str__(self):
        return f"Semestre {self.semestre}"
