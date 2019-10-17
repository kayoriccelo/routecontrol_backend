from django.db.models import Q
from rest_framework import serializers

from .models import UserRotarization


class UserRotarizationSerializer(serializers.Serializer):
    fields_required = ['first_name', 'last_name', 'cpf', 'username', 'email', 'password']

    def validate(self, attrs):
        data = self.context['request'].data
        
        criticas = []
        for field in self.fields_required:
            if not field in data:
                criticas.append(f'{field} não informado.')

        if len(criticas) > 0:
            raise serializers.ValidationError(criticas)

        try:
            UserRotarization.objects.get(
                Q(cpf=data['cpf']), 
                Q(username=data['username']), 
                Q(email=data['email'])
            )

            raise serializers.ValidationError(u'Conta já cadastrado.')
        except UserRotarization.DoesNotExist:
            pass

        return attrs

    def save(self, **kwargs):
        data = self.context['request'].data

        try:
            user_rotarization = UserRotarization(
                cpf=data['cpf'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                username=data['username'],
                is_active=True,
                is_staff=False
            )
            user_rotarization.set_password(data['password'])
            user_rotarization.save()
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': [u'Não foi possível registrar uma nova conta. Error: ' + e.args[0]]})

        return user_rotarization