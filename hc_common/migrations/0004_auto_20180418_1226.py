# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-04-18 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0003_auto_20180307_0842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationtype',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='educationtype',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]