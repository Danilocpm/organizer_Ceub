from django.db import models
from .professores import Professor
from .diasdasemana import DiasDaSemana
from .campus import Campus  

class Disponibilidade(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    dia_da_semana = models.ForeignKey(DiasDaSemana, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, null=True, blank=True)
    observacao = models.TextField(blank=True, null=True)  # Permite valores em branco e nulos

    class Meta:
        unique_together = ('professor', 'dia_da_semana', 'campus')

    def __str__(self):
        return f"{self.professor} - {self.dia_da_semana} - {self.campus}"
