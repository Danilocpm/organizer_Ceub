from rest_framework.routers import DefaultRouter
from ..views.professoresViews import ProfessorViewSet

# Cria um router e registra o viewset
router = DefaultRouter()
router.register(r'api/professores', ProfessorViewSet)

# As URLs são geradas automaticamente pelo router
urlpatterns = router.urls