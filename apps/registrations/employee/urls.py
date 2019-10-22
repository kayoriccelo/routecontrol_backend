from rest_framework.routers import DefaultRouter

from .viewsets import EmployeeViewSet


router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
