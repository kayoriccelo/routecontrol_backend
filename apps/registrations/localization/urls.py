from rest_framework.routers import DefaultRouter

from .viewsets import LocalizationViewSet


router = DefaultRouter()
router.register(r'localization', LocalizationViewSet)
