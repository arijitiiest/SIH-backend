from rest_framework import routers
from .api import AdminRoadViewSet

router = routers.DefaultRouter()
router.register('api/admin/roads', AdminRoadViewSet, 'roads')

urlpatterns = router.urls