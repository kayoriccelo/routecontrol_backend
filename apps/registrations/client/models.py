import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    cnpj = models.CharField(_('Cnpj'), max_length=14)
    business_name = models.CharField(_(u'Razão social'), max_length=140)
    date_registred = models.DateField(_('Data de Cadastro'), default=datetime.date.today)
    email = models.EmailField(_('Email'), null=True, blank=True)
    phone = models.CharField(_('Telefone'), max_length=20, null=True, blank=True)

    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), null=True, related_name='clients',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
        db_table = 'client'
