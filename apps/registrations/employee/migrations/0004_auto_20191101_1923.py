# Generated by Django 2.2.6 on 2019-11-01 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20191026_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='company.Company', verbose_name='Empresa'),
        ),
    ]