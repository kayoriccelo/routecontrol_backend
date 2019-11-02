from ...core.serializers import BaseSerializer
from .models import Employee


class EmployeeSerializer(BaseSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
