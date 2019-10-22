from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ...core.mixins import ListPaginationMixin
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet, ListPaginationMixin):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)

    def get_queryset(self):
        company = Company.objects.filter(employees__cpf=self.request._user.cpf)
        return company