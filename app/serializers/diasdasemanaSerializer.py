from rest_framework import serializers
from ..models import DiasDaSemana

class DiasDaSemanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiasDaSemana
        fields = ['id', 'day', 'turno'] 