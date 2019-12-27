# Generated by Django 2.2 on 2019-08-14 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0009_auto_20190717_1543'),
        ('hc_practicas', '0002_auto_20190717_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='bornPlace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hc_common.Country'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='civilStatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hc_common.CivilStatusType'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hc_common.EducationType'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='occupation',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profesional',
            name='postal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profesional',
            name='socialService',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hc_common.SocialService'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='socialServiceNumber',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profesional',
            name='street',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]