from rest_framework import routers
from .api import RoadViewSet

router = routers.DefaultRouter()
router.register('api/roads', RoadViewSet, 'roads')

urlpatterns = router.urls
