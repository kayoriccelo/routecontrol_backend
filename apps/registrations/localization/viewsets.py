from ...core.viewsets import BaseViewSet
from .models import Localization
from ..company.models import Company
from .serializers import LocalizationSerializer


class LocalizationViewSet(BaseViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer
    
    def get_queryset(self):
        try:
            company = Company.objects.get(employees__cpf=self.request._user.cpf)
        except Company.DoesNotExist:
            company = None
        
        kwargs = {}
        
        if 'ids' in self.request.query_params:
            kwargs['id__in'] = self.request.query_params['ids'].split(',')
        return self.queryset.filter(company=company).filter(**kwargs)
