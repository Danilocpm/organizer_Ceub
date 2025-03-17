from rest_framework import serializers
from ..models import Turma

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id', 'professor', 'materia', 'dia_da_semana', 'sala'] 