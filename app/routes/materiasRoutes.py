from rest_framework.routers import DefaultRouter
from ..views.materiasViews import MateriaViewSet

router = DefaultRouter()
router.register(r'api/materias', MateriaViewSet)

urlpatterns = router.urls
