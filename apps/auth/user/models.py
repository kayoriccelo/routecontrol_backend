from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserRotarization(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    first_access = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    company = models.ForeignKey('company.Company', verbose_name=_('Empresa'), related_name='users',
                                blank=True, null=True, on_delete=None)

    REQUIRED_FIELDS = ['email', 'cpf']

    class Meta:
        verbose_name = ('user rotarization')
        verbose_name_plural = ('users rotarization')
        db_table = 'user_rotarization'
        ordering = ['cpf',]
