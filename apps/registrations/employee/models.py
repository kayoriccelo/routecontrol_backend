import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ...auth.user.models import UserRotarization


class Employee(models.Model):
    cpf = models.CharField(_(u'Cpf'), max_length=11, null=True)
    name = models.CharField(_(u'Nome'), max_length=140, null=True)
    date_registred = models.DateField(_('Data de Cadastro'), default=datetime.date.today)
    email = models.EmailField(_('Email'), null=True, blank=True)
    phone = models.CharField(_('Telefone'), max_length=20, null=True, blank=True)
    
    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), related_name='employees',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')
        db_table = 'employee'
