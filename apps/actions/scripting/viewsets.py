from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from ...core.mixins import ListPaginationMixin, FilterForCompanyMixin
from .models import Scripting
from .serializers import ScriptingSerializer


class ScriptingViewSet(viewsets.ModelViewSet, ListPaginationMixin, FilterForCompanyMixin):
    queryset = Scripting.objects.all()
    serializer_class = ScriptingSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('id',)
