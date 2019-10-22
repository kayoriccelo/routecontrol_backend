from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.auth.user.urls import router as user_routers
from apps.registrations.company.urls import router as company_routers
from apps.registrations.employee.urls import router as employee_routers


router = DefaultRouter()

urlpatterns = (
    router.urls + 
    user_routers.urls +
    company_routers.urls +
    employee_routers.urls
)
