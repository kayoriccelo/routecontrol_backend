from rest_framework import serializers

from .mixins import IncludeCompanyMixin


class BaseSerializer(serializers.ModelSerializer, IncludeCompanyMixin):
    def create(self, validated_data):
        instance = super(BaseSerializer, self).create(validated_data)
        self.include(instance, self.context['request'])

        return instance
