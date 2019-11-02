from ...core.serializers import BaseSerializer
from .models import Localization


class LocalizationSerializer(BaseSerializer):
    class Meta:
        model = Localization
        fields = '__all__'
