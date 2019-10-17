from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.auth.user.urls import router as users_router


router = DefaultRouter()

urlpatterns = (
    router.urls + 
    users_router.urls
)
