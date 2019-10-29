import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Scripting(models.Model):
    description = models.CharField(_('Descrição'), max_length=300)
    date_initial = models.DateField(_('Início'), null=True)
    date_final = models.DateField(_('Fim'), null=True)
    date_registred = models.DateField(_('Data de Cadastro'), default=datetime.date.today)
    origin_latitude = models.CharField(_('Origen Latitude'), max_length=100, null=True)
    origin_longitude = models.CharField(_('Origen Longitude'), max_length=100, null=True)
    origin_address = models.CharField(_('Origen Endereço'), max_length=300, null=True)
    destiny_latitude = models.CharField(_('Destino Latitude'), max_length=100, null=True)
    destiny_longitude = models.CharField(_('Destino Longitude'), max_length=100, null=True)
    destiny_address = models.CharField(_('Destino Endereço'), max_length=300, null=True)

    localizations = models.ManyToManyField('localization.Localization', 
        verbose_name='localization', related_name="scripting", null=True)
    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), null=True, 
                                related_name='scriptings', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Roteirização')
        verbose_name_plural = _('Roteirizações')
        db_table = 'scripting'
