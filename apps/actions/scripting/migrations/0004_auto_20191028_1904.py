# Generated by Django 2.2.6 on 2019-10-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripting', '0003_auto_20191028_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripting',
            name='date_final',
            field=models.DateField(null=True, verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='scripting',
            name='date_initial',
            field=models.DateField(null=True, verbose_name='Início'),
        ),
    ]
