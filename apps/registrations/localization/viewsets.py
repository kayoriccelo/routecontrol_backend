from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ...core.mixins import ListPaginationMixin, FilterForCompanyMixin
from .models import Localization
from .serializers import LocalizationSerializer


class LocalizationViewSet(viewsets.ModelViewSet, ListPaginationMixin, FilterForCompanyMixin):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    
    def get_queryset(self):
        kwargs = {}
        
        if 'ids' in self.request.query_params:
            kwargs['id__in'] = self.request.query_params['ids'].split(',')
        return self.queryset.filter(**kwargs)
