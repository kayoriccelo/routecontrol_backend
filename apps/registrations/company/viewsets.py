from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Company
from ..employee.models import Employee
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def _get_company(self, user):
        if user.company:
            return user.company
        else:
            try:
                return Employee.objects.get(cpf=user.cpf).company
            except:
                raise serializers.ValidatorError({'non_field_errors': ['Cpf cadastrado em mais de uma empresa.']})
    
    def get_queryset(self):
        company = self._get_company(self.request.user)

        company_id = company.id if company else -1

        return self.queryset.filter(id=company_id)
