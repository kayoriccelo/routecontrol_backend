from ...core.serializers import BaseSerializer
from .models import Scripting


class ScriptingSerializer(BaseSerializer):
    class Meta:
        model = Scripting
        fields = '__all__'
