# Generated by Django 2.2 on 2019-11-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_hce', '0007_auto_20190910_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Importation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(upload_to='')),
                ('createdOn', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
