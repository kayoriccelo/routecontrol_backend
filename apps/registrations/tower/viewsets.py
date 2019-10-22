from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ...core.mixins import ListPaginationMixin, FilterForCompanyMixin
from .models import Tower
from .serializers import TowerSerializer


class TowerViewSet(viewsets.ModelViewSet, ListPaginationMixin, FilterForCompanyMixin):
    queryset = Tower.objects.all()
    serializer_class = TowerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
