from rest_framework import serializers
from collections import OrderedDict
from django.db.models import Count
from apps.registrations.client.models import Client
from apps.registrations.employee.models import Employee
from apps.registrations.localization.models import Localization
from apps.actions.scripting.models import Scripting


class DashboardSerializer(serializers.Serializer):

    def _get_company(self):
        user = self.context['user']

        if user.company:
            return user.company
        else:
            try:
                return Employee.objects.get(cpf=user.cpf).company
            except Employee.DoesNotExist:
                raise serializers.ValidatorError({'non_field_errors': [f'Empregado não encontrado com esse cpf: {user.cpf}.']})
            except:
                raise serializers.ValidatorError({'non_field_errors': ['Cpf cadastrado em mais de uma empresa.']})

    def incrementa_item(self, field, values, label):
        colors = [
            'fill-color: #00344d; fill-opacity: 0.7;',
            'fill-color: #004666; fill-opacity: 0.7;',
            'fill-color: #005074; fill-opacity: 0.7;',
            'fill-color: #005780; fill-opacity: 0.7;',
            'fill-color: #006999; fill-opacity: 0.7;',
            'fill-color: #007ab3; fill-opacity: 0.7;',
            'fill-color: #008bcc; fill-opacity: 0.7;',
            'fill-color: #009de6; fill-opacity: 0.7;',
            'fill-color: #00aeff; fill-opacity: 0.7;',
            'fill-color: #1ab6ff; fill-opacity: 0.7;',
        ]

        ret = [["Element", label, {"role": "style"}, {"role": "style"}]]

        for index, value in enumerate(values):
            item = [
                value[field],
                value['count'],
                colors[index],
                'opacity: 0.2'
            ]
            ret.append(item)

        return ret

    def to_representation(self, instance):
        company = self._get_company()

        params = {'company': company}

        # clients = Scripting.objects.filter(**params)

        routes_employees = Scripting.objects.filter(**params).values('employees__name').annotate(
            count=Count('employees__name')).order_by('-employees__name')[:10]

        routes_clients = Scripting.objects.filter(**params).values('localizations__client__business_name').annotate(
            count=Count('localizations__client__business_name')).order_by('-localizations__client__business_name')[:10]

        # localizations = Localization.objects.filter(**params)

        # employees = Employee.objects.filter(**params).values('journey__description').annotate(
        #     count=Count('journey__description')).order_by('-name')[:10]

        # points = PointMarking.objects.filter(employee__company=params['company']).values(
        #     'employee__journey__description').annotate(count=Count('employee__journey__description')).order_by(
        #     '-employee__journey__description')[:10]

        dashboard_dict = OrderedDict()
        dashboard_dict['employees'] = self.incrementa_item('employees__name', routes_employees, 'Roteirizações')
        dashboard_dict['clients'] = self.incrementa_item('localizations__client__business_name', routes_clients, 'Roteirizações')

        return dashboard_dict