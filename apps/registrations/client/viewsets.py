from ...core.viewsets import BaseViewSet
from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(BaseViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_fields = ('id',)
