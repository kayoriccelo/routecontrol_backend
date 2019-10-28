from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..client.models import Client
from ..company.models import Company

PEDDING = 'P'
COMPLETED = 'C'

STATUS = (
    (PEDDING, 'Pendente'),
    (COMPLETED, 'Concluído'),
)

class Localization(models.Model):
    code = models.CharField(_('Código'), max_length=10)
    description = models.CharField(_('Descrição'), max_length=300)
    latitude = models.CharField(_('Latitude'), max_length=100, null=True)
    longitude = models.CharField(_('Longitude'), max_length=100, null=True)
    address = models.CharField(_('Endereço'), max_length=300, null=True)

    client = models.OneToOneField(Client, verbose_name=_("Cliente"), null=True, 
                                related_name='localizations', on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), null=True, 
                                related_name='localizations', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Localização')
        verbose_name_plural = _('Localizações')
        db_table = 'localization'
