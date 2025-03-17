from rest_framework import viewsets
from ..models import Disponibilidade
from ..serializers import DisponibilidadeSerializer

class DisponibilidadeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Disponibilidade.
    """
    queryset = Disponibilidade.objects.all()
    serializer_class = DisponibilidadeSerializer
