from django.db import models
from .professores import Professor
from .materias import Materia

class Adesao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True)  # Permite valores em branco e nulos

    class Meta:
        unique_together = ('professor', 'materia')

    def __str__(self):
        return f"{self.professor} - {self.materia}"
