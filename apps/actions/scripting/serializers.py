from rest_framework import serializers

from ...core.serializers import BaseSerializer
from .models import Scripting


class ScriptingSerializer(BaseSerializer):
    localizations_count = serializers.CharField(read_only=True)
    employees_count = serializers.CharField(read_only=True)
    date_initial = serializers.DateField(
        required=False, allow_null=True, format='%Y-%m-%d', input_formats=['', '%d/%m/%Y', '%Y-%m-%d'])
    hour_initial = serializers.TimeField(
        required=False, allow_null=True, format='%H:%M', input_formats=['', '%H:%M'])
    date_final = serializers.DateField(
        required=False, allow_null=True, format='%Y-%m-%d', input_formats=['', '%d/%m/%Y', '%Y-%m-%d'])
    hour_final = serializers.TimeField(
        required=False, allow_null=True, format='%H:%M', input_formats=['', '%H:%M'])

    class Meta:
        model = Scripting
        fields = '__all__'
