from rest_framework.routers import DefaultRouter

from .viewsets import TowerViewSet


router = DefaultRouter()
router.register(r'tower', TowerViewSet)
