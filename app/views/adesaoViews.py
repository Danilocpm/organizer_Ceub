from rest_framework import viewsets
from ..models import Adesao
from ..serializers import AdesaoSerializer

class AdesaoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on Adesao.
    """
    queryset = Adesao.objects.all()
    serializer_class = AdesaoSerializer
