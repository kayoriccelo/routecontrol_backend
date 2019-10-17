from rest_framework.routers import DefaultRouter

from .viewsets import UserRotarizationCreateViewSet


router = DefaultRouter()
router.register(r'usercreate', UserRotarizationCreateViewSet)
 