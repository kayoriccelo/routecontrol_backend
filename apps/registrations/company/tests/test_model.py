from .base import CompanyBaseTestCase
from apps.registrations.company.models import Company


class CompanyTestCase(CompanyBaseTestCase):

    def test_01_create(self):
        company_created = self._create()
        company = Company.objects.first()

        self.assertEqual(company, company_created)

    def test_02_update(self):
        company = Company.objects.first()
        business_name = company.business_name

        company.business_name = 'Updated company test'
        company.save()

        self.assertFalse(business_name == company.business_name)

    def test_03_delete(self):
        company = Company.objects.first()
        company.delete()

        count = Company.objects.count()

        self.assertEqual(count, 0)
