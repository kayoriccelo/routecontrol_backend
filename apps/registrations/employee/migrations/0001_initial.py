# Generated by Django 2.2.6 on 2019-10-22 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, null=True, verbose_name='Cpf')),
                ('name', models.CharField(max_length=140, null=True, verbose_name='Nome')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.Company', verbose_name='Empresa')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
                'db_table': 'employee',
            },
        ),
    ]
