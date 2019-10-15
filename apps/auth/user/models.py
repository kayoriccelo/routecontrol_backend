from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRoterization(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    first_access = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'cpf']

    class Meta:
        verbose_name = ('user roterization')
        verbose_name_plural = ('users roterization')
        db_table = 'user_roterization'
        ordering = ['cpf',]