from rest_framework.routers import DefaultRouter
from ..views.turmaViews import TurmaViewSet

router = DefaultRouter()
router.register(r'api/turmas', TurmaViewSet)

urlpatterns = router.urls
