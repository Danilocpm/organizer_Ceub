from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from ..models import Professor
from ..serializers.professoresSerializer import ProfessorSerializer  # Updated import

class ProfessorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operações CRUD em Professor.
    Fornece automaticamente as ações:
    'list', 'create', 'retrieve', 'update', 'partial_update', 'destroy'
    """
    queryset = Professor.objects.all().order_by('name')
    serializer_class = ProfessorSerializer
    
    # Adiciona parsers para permitir o upload de arquivos
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    @action(detail=True, methods=['patch'])
    def upload_photo(self, request, pk=None):
        """
        Endpoint personalizado para atualizar apenas a foto do professor
        PATCH /api/professores/{id}/upload_photo/
        """
        professor = self.get_object()
        
        if 'icon_photo' in request.FILES:
            professor.icon_photo = request.FILES['icon_photo']
            professor.save()
            
            serializer = self.get_serializer(professor)
            return Response(serializer.data)
        
        return Response(
            {'error': 'Nenhuma foto enviada'},
            status=status.HTTP_400_BAD_REQUEST
        )