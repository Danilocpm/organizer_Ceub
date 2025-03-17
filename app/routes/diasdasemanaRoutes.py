from rest_framework.routers import DefaultRouter
from ..views.diasdasemanaViews import DiasDaSemanaViewSet

router = DefaultRouter()
router.register(r'api/dias-da-semana', DiasDaSemanaViewSet)

urlpatterns = router.urls