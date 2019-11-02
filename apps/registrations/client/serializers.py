from ...core.serializers import BaseSerializer
from .models import Client


class ClientSerializer(BaseSerializer):
    class Meta:
        model = Client
        fields = '__all__'
