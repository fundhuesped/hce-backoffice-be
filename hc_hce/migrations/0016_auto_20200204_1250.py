# Generated by Django 2.2 on 2020-02-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_hce', '0015_auto_20191226_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importationdeterminationrelationship',
            name='determination_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='importationregister',
            name='determination_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
