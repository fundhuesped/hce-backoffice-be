# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-05-30 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0004_auto_20180418_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='alias',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
