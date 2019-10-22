from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    cnpj = models.CharField(_('Cnpj'), max_length=14)
    business_name = models.CharField(_(u'Razão social'), max_length=140)
    email = models.EmailField(_('Email'), null=True, blank=True)
    phone = models.CharField(_('Telefone'), max_length=20, null=True, blank=True)
    
    class Meta:
        verbose_name = _('Empresa')
        db_table = 'company'
