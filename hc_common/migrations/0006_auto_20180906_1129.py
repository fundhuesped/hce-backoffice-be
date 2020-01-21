# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-09-06 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0005_persona_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='bornPlace',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='civilStatus',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='documentType',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='education',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='genderAtBirth',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='genderOfChoice',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='location',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='socialService',
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
