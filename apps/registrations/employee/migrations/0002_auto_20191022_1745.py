# Generated by Django 2.2.6 on 2019-10-22 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='company.Company', verbose_name='Empresa'),
        ),
    ]
