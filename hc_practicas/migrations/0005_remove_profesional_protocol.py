# Generated by Django 2.2 on 2020-01-21 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hc_practicas', '0004_profesional_protocol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesional',
            name='protocol',
        ),
    ]
