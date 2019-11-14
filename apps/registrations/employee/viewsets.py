from ...core.viewsets import BaseViewSet
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(BaseViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_fields = ('id',)
    search_fields = ('cpf', 'name')

    def get_queryset(self):
        queryset = super(EmployeeViewSet, self).get_queryset()
        
        kwargs = {}
        
        if 'ids' in self.request.query_params:
            kwargs['id__in'] = self.request.query_params['ids'].split(',')
        
        return queryset.filter(**kwargs)
