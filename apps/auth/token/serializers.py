from django.utils.six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.registrations.employee.models import Employee
from ..user.models import UserRotarization


class TokenCustomSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenCustomSerializer, self).validate(attrs)
        refresh = self.get_token(self.user)

        try:
            UserRotarization.objects.get(cpf=self.user.cpf, is_superuser=False)
        except UserRotarization.DoesNotExist:
            raise serializers.ValidationError(u'Not Authorized.')

        try:
            employee = Employee.objects.get(cpf=self.user.cpf)
        except Employee.DoesNotExist:
            employee = None

        try:
            user = UserRotarization.objects.get(cpf=self.user.cpf, is_admin=True)
        except UserRotarization.DoesNotExist:
            user = None

        if not user and not employee:
            raise serializers.ValidationError(u'Aguardando autorização.')

        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)

        return data
