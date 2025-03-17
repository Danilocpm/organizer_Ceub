from rest_framework import serializers
from ..models import Disponibilidade

class DisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidade
        fields = ['id', 'professor', 'dia_da_semana', 'campus'] 