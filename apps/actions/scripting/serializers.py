from rest_framework import serializers

from .models import Scripting


class ScriptingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripting
        fields = '__all__'
