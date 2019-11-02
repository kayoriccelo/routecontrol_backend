from rest_framework.response import Response

from ..registrations.company.models import Company
from ..registrations.employee.models import Employee


class ListPaginationMixin(object):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FilterForCompanyMixin(object):
    def _get_company(self, user):
        if user.company:
            return user.company
        else:
            try:
                return Employee.objects.get(cpf=user.cpf).company
            except Employee.DoesNotExist:
                raise serializers.ValidatorError({'non_field_errors': [f'Empregado não encontrado com esse cpf: {user.cpf}.']})
            except:
                raise serializers.ValidatorError({'non_field_errors': ['Cpf cadastrado em mais de uma empresa.']})

    def get_queryset(self):
        company = self._get_company(self.request.user)

        return self.queryset.filter(company=company)


class IncludeCompanyMixin(object):
    def _get_company(self, user):
        if user.company:
            return user.company
        else:
            try:
                return Employee.objects.get(cpf=user.cpf)
            except:
                raise serializers.ValidatorError({'non_field_errors': ['Cpf cadastrado em mais de uma empresa.']})

    def include(self, instance, request):
        company = self._get_company(request.user)
        if not company:
            raise serializers.ValidatorError({'non_field_errors': ['Empresa não encontrada.']})

        instance.company = company
        instance.save()
