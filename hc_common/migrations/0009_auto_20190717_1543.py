# Generated by Django 2.2 on 2019-07-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0008_auto_20190403_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilstatustype',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='country',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hc_common.Province'),
        ),
        migrations.AlterField(
            model_name='district',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='educationtype',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hc_common.District'),
        ),
        migrations.AlterField(
            model_name='location',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='province',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='sextype',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='status',
            field=models.CharField(choices=[('Active', 'Activo'), ('Inactive', 'Inactivo')], default='Active', max_length=8),
        ),
    ]