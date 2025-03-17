from rest_framework.routers import DefaultRouter
from ..views.adesaoViews import AdesaoViewSet

router = DefaultRouter()
router.register(r'api/adesoes', AdesaoViewSet)

urlpatterns = router.urls
