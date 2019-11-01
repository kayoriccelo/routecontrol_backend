from .models import Client

from ...core.serializers import BaseSerializer


class ClientSerializer(BaseSerializer):
    class Meta:
        model = Client
        fields = '__all__'
