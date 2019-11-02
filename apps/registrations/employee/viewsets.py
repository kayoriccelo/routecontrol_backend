from ...core.viewsets import BaseViewSet
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(BaseViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_fields = ('id',)
