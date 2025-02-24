from django.db import models
from .professores import Professor
from .diasdasemana import DiasDaSemana

class Disponibilidade(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    dia_da_semana = models.ForeignKey(DiasDaSemana, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('professor', 'dia_da_semana')

    def __str__(self):
        return f"{self.professor} - {self.dia_da_semana}"
