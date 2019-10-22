from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.auth.user.urls import router as user_routers
from apps.registrations.company.urls import router as company_routers


router = DefaultRouter()

urlpatterns = (
    router.urls + 
    user_routers.urls +
    company_routers.urls
)
