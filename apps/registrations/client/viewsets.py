from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ...core.mixins import ListPaginationMixin, FilterForCompanyMixin
from .models import Client
from ..company.models import Company
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet, ListPaginationMixin):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)

    def get_queryset(self):
        company = Company.objects.get(employees__cpf=self.request._user.cpf)
        
        return self.queryset.filter(company=company)
