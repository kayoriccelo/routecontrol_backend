from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        try:
            company = Company.objects.get(employees__cpf=self.request._user.cpf).id
        except Company.DoesNotExist:
            company = -1
        
        return self.queryset.filter(id=company)
