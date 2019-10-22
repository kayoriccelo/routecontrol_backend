from django.db import models
from django.utils.translation import ugettext_lazy as _

from ...auth.user.models import UserRotarization


class Employee(models.Model):
    cpf = models.CharField(_(u'Cpf'), max_length=11, null=True)
    name = models.CharField(_(u'Nome'), max_length=140, null=True)
    
    user = models.OneToOneField(UserRotarization, verbose_name=_("Usuário"), null=True, related_name='users',
                                on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), null=True, related_name='employees',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')
        db_table = 'employee'