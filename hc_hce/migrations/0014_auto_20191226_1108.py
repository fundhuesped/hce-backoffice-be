# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-04-05 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_hce', '0013_auto_20191226_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='ImportationPatientRelationship',
            name='gender',
            field=models.CharField(choices=[('M','MASCULINO'), ('F','FEMENINO')], default='M', max_length=1),
        ),
    ]