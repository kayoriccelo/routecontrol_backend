from django.db.models import Q
from rest_framework import serializers

from .models import UserRotarization


class UserRotarizationCreateSerializer(serializers.Serializer):
    fields_required = [
        ('first_name', 'Primeiro Nome'),
        ('last_name', 'Ultimo Nome'),
        ('cpf', 'Cpf'),
        ('username', 'Usuário'),
        ('email', 'Email'),
        ('password', 'Senha')
    ]

    def validate(self, attrs):
        data = self.context['request'].data

        criticas = []
        for field in self.fields_required:
            if not field[0] in data:
                criticas.append(f'{field[1]} não informado.')
                continue

            attrs[field[0]] = data[field[0]]

        if len(criticas) > 0:
            raise serializers.ValidationError(criticas)

        try:
            UserRotarization.objects.get(
                Q(cpf=attrs['cpf']),
                Q(username=attrs['username']),
                Q(email=attrs['email'])
            )

            raise serializers.ValidationError(u'Conta já cadastrado.')
        except UserRotarization.DoesNotExist:
            pass

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')

        try:
            user_rotarization = UserRotarization(
                **validated_data,
                is_active=True,
                is_staff=False
            )

            user_rotarization.set_password(password)
            user_rotarization.save()
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': [
                u'Não foi possível registrar uma nova conta.'
            ]})

        return user_rotarization
 

class UserRotarizationSerializer(serializers.ModelSerializer):
     class Meta:
        model = UserRotarization
        fields = ['id', 'first_name', 'last_name', 'cpf', 'is_admin']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRotarization
        fields = ('id', 'first_name', 'last_name')

    def validate(self, attrs):

        if 'new_password' in self.context['request'].data:
            attrs['new_password'] = self.context['request'].data['new_password']

        return attrs

    def update(self, instance, validated_data):
        try:
            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            if 'new_password' in validated_data:
                instance.set_password(validated_data['new_password'])
            instance.save()
        except Exception as e:
            raise serializers.ValidationError({'non_field_errors': [u'Não foi possível salvar o perfil. ']})

        return instance
