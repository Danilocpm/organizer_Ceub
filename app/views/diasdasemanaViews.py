from rest_framework import viewsets
from ..models import DiasDaSemana
from ..serializers import DiasDaSemanaSerializer

class DiasDaSemanaViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on DiasDaSemana.
    """
    queryset = DiasDaSemana.objects.all().order_by('day', 'turno')
    serializer_class = DiasDaSemanaSerializer 