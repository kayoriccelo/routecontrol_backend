# Generated by Django 2.2.6 on 2019-10-26 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_registred',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Cadastro'),
        ),
    ]
