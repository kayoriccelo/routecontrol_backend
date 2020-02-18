from django.test import TestCase, RequestFactory

from apps.registrations.company.models import Company


class CompanyBaseTestCase(TestCase):
    def setUp(self):
        pass

    def setDown(self):
        pass

    def _create(self):
        return Company.objects.create(cnpj='05481245674154', business_name='Company created test')
