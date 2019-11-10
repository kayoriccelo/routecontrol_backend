import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

DISREGARDED = 'D'
PEDDING = 'P'
IN_PROGRESS = 'I'
COMPLETED = 'C'

STATUS = (
    (DISREGARDED, 'Desconsiderado'),
    (PEDDING, 'Pendente'),
    (IN_PROGRESS, 'Em andamento'),
    (COMPLETED, 'Concluído'),
)


class Scripting(models.Model):
    description = models.CharField(_('Descrição'), max_length=300)
    date_initial = models.DateField(_('Data Início'), null=True, blank=True)
    hour_initial = models.TimeField(_('Hora Início'), null=True, blank=True)
    date_final = models.DateField(_('Data Fim'), null=True, blank=True)
    hour_final = models.TimeField(_('Hora Fim'), null=True, blank=True)
    date_registred = models.DateField(
        _('Data de Cadastro'), default=datetime.date.today)
    origin_latitude = models.CharField(
        _('Origen Latitude'), max_length=100, null=True)
    origin_longitude = models.CharField(
        _('Origen Longitude'), max_length=100, null=True)
    origin_address = models.CharField(
        _('Origen Endereço'), max_length=300, null=True)
    destiny_latitude = models.CharField(
        _('Destino Latitude'), max_length=100, null=True)
    destiny_longitude = models.CharField(
        _('Destino Longitude'), max_length=100, null=True)
    destiny_address = models.CharField(
        _('Destino Endereço'), max_length=300, null=True)
    status = models.CharField(
        _('Situação'), max_length=1, choices=STATUS, default=PEDDING)

    localizations = models.ManyToManyField('localization.Localization',
                                           verbose_name='localization', related_name="scripting", blank=True)
    employees = models.ManyToManyField('employee.Employee',
                                       verbose_name='employee', related_name="scripting", blank=True)
    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'),
                                related_name='scriptings', on_delete=models.CASCADE)

    @property
    def localizations_count(self):
        return self.localizations.count()

    @property
    def employees_count(self):
        return self.employees.count()

    class Meta:
        verbose_name = _('Roteirização')
        verbose_name_plural = _('Roteirizações')
        db_table = 'scripting'
