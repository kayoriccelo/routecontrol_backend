from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ...core.mixins import ListPaginationMixin, FilterForCompanyMixin
from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet, ListPaginationMixin, FilterForCompanyMixin):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)
