# Generated by Django 2.2 on 2019-07-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hc_pacientes', '0003_auto_20181217_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='consent',
            field=models.CharField(choices=[('Yes', 'Si'), ('No', 'No'), ('Not asked', 'No preguntado')], default='Not asked', max_length=14),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='documentType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hc_common.DocumentType'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fatherSurname',
            field=models.CharField(default='No informado', max_length=80),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='firstName',
            field=models.CharField(default='No informado', max_length=80),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
    ]
