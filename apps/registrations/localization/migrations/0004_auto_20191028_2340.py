# Generated by Django 2.2.6 on 2019-10-28 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localization', '0003_localization_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localization',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localizations', to='client.Client', verbose_name='Cliente'),
        ),
    ]
