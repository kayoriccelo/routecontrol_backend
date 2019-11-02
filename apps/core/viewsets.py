from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .mixins import ListPaginationMixin, FilterForCompanyMixin


class BaseViewSet(FilterForCompanyMixin, ListPaginationMixin, viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
