from rest_framework.response import Response

from ..registrations.company.models import Company


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
    def get_queryset(self):
        try:
            company = Company.objects.get(employees__cpf=self.request._user.cpf)
        except Company.DoesNotExist:
            company = None
        
        return self.queryset.filter(company=company)


class IncludeCompanyMixin(object):
    def include(self, instance, request):
        try:
            company = Company.objects.get(employees__cpf=request.user.cpf)
        except Company.DoesNotExist:
            raise serializers.ValidatorError({'non_field_errors': ['Empresa não encontrada.']})

        instance.company = company
        instance.save()
