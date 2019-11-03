from rest_framework import serializers

from ...core.serializers import BaseSerializer
from .models import Scripting


class ScriptingSerializer(BaseSerializer):
    localizations_count = serializers.CharField(read_only=True)

    class Meta:
        model = Scripting
        fields = '__all__'
