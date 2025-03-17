from rest_framework import viewsets
from ..models import Materia
from ..serializers import MateriaSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Materia.
    Provides 'list', 'create', 'retrieve', 'update', 'partial_update', 'destroy'
    """
    queryset = Materia.objects.all().order_by('semester', 'name')
    serializer_class = MateriaSerializer
