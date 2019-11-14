from ...core.viewsets import BaseViewSet
from .models import Localization
from ..company.models import Company
from .serializers import LocalizationSerializer


class LocalizationViewSet(BaseViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer
    filter_fields = ('id',)
    search_fields = ('code', 'description')
    
    def get_queryset(self):
        queryset = super(LocalizationViewSet, self).get_queryset()
        
        kwargs = {}
        
        if 'ids' in self.request.query_params:
            kwargs['id__in'] = self.request.query_params['ids'].split(',')
        
        return queryset.filter(**kwargs)
