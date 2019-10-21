from rest_framework.routers import DefaultRouter

from .viewsets import UserRotarizationCreateViewSet, UserRotarizationViewSet


router = DefaultRouter()
router.register(r'usercreate', UserRotarizationCreateViewSet)
router.register(r'user', UserRotarizationViewSet) 