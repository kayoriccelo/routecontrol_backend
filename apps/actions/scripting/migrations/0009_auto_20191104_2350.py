# Generated by Django 2.2.6 on 2019-11-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripting', '0008_scripting_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='scripting',
            name='hour_final',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Fim'),
        ),
        migrations.AddField(
            model_name='scripting',
            name='hour_initial',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora Início'),
        ),
        migrations.AlterField(
            model_name='scripting',
            name='date_final',
            field=models.DateField(blank=True, null=True, verbose_name='Data Fim'),
        ),
        migrations.AlterField(
            model_name='scripting',
            name='date_initial',
            field=models.DateField(blank=True, null=True, verbose_name='Data Início'),
        ),
        migrations.AlterField(
            model_name='scripting',
            name='status',
            field=models.CharField(choices=[('D', 'Desconsiderado'), ('P', 'Pendente'), ('I', 'Em andamento'), ('C', 'Concluído')], default='P', max_length=1, verbose_name='Situação'),
        ),
    ]
