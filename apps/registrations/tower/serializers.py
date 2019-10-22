from rest_framework import serializers

from .models import Tower


class TowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tower
        fields = '__all__'
