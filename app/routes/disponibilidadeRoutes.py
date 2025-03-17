from rest_framework.routers import DefaultRouter
from ..views.disponibilidadeViews import DisponibilidadeViewSet

router = DefaultRouter()
router.register(r'api/disponibilidades', DisponibilidadeViewSet)

urlpatterns = router.urls
