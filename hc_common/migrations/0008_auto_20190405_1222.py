# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-04-05 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0007_auto_20181217_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialservice',
            options={'ordering': ['-order', 'name']},
        ),
    ]
