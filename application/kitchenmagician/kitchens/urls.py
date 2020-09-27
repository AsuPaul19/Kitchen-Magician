from rest_framework import routers
from .api import KitchenViewSet

router = routers.DefaultRouter()
router.register('api/kitchens', KitchenViewSet, 'kitchens')

urlpatterns = router.urls
