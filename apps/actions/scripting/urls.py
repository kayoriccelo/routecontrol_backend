from rest_framework.routers import DefaultRouter

from .viewsets import ScriptingViewSet


router = DefaultRouter()
router.register(r'scripting', ScriptingViewSet)
