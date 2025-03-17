from rest_framework import serializers
from ..models import Adesao

class AdesaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adesao
        fields = ['id', 'professor', 'materia', 'observacao'] 