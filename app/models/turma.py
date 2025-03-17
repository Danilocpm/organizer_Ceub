from django.db import models
from .professores import Professor
from .materias import Materia
from .diasdasemana import DiasDaSemana

class Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    dia_da_semana = models.ForeignKey(DiasDaSemana, on_delete=models.CASCADE)
    sala = models.CharField(max_length=20) 

    class Meta:
        unique_together = ('professor', 'materia', 'dia_da_semana')

    def __str__(self):
        return f"{self.materia} - {self.professor} - {self.sala}"
