from rest_framework.routers import DefaultRouter

from .views import ArchiveViewSet, LabViewSet

router = DefaultRouter()

router.register(r'labs', LabViewSet, basename='labs')
router.register(r'archive', ArchiveViewSet, basename='archive')

urlpatterns = router.urls