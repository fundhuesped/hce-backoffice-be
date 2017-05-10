# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 01:16
from __future__ import unicode_literals

from django.db import migrations
import io


def loadInitialData(filename):
    with io.open('./hc_common/migrations/initial_data/' + filename + '.sql', 'r', encoding='utf8') as file:
        return file.read()


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(loadInitialData('sextype')),
        migrations.RunSQL(loadInitialData('civilstatustype')),
        migrations.RunSQL(loadInitialData('educationtype')),
        migrations.RunSQL(loadInitialData('documenttype')),
        migrations.RunSQL(loadInitialData('province')),
        migrations.RunSQL(loadInitialData('district')),
        migrations.RunSQL(loadInitialData('location'))
    ]
