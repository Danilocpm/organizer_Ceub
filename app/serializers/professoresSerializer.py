from rest_framework import serializers
from ..models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Professor.
    Converte objetos Professor para JSON e vice-versa.
    """
    class Meta:
        model = Professor
        fields = ['id', 'name', 'lastname', 'email', 'icon_photo']
        read_only_fields = ['id'] 