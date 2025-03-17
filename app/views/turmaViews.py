from rest_framework import viewsets
from ..models import Turma
from ..serializers import TurmaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Turma.
    """
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
