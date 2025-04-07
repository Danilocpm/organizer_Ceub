from django.db import models
from .professores import Professor
from .materias import Materia
from .diasdasemana import DiasDaSemana
from .campus import Campus

class Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    dia_da_semana = models.ForeignKey(DiasDaSemana, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True) # Added campus ForeignKey, allow null
    sala = models.CharField(max_length=20)
    tag = models.CharField(max_length=3, null=True, blank=True) # Added tag field, allow null

    class Meta:
        # Updated unique_together to include campus
        unique_together = ('professor', 'materia', 'dia_da_semana', 'campus')

    def __str__(self):
        # Updated __str__ to include campus
        return f"{self.materia} - {self.professor} - {self.campus} - {self.sala}"
