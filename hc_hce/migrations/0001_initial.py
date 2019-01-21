# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-09-06 14:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hc_pacientes', '__first__'),
        ('hc_masters', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientARVPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescripctionType', models.CharField(choices=[(b'Vaccine', b'Vaccine'), (b'Arv', b'Arv'), (b'Prophylaxis', b'Prophylaxis'), (b'General', b'General')], default=b'General', max_length=20)),
                ('observations', models.CharField(max_length=200, null=True)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('issuedDate', models.DateField()),
                ('duplicateRequired', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
            ],
            options={
                'ordering': ['-createdOn'],
            },
        ),
        migrations.CreateModel(
            name='PatientARVPrescriptionMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityPerDay', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('quantityPerMonth', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('medication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_masters.Medication')),
                ('prescription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescriptedMedications', to='hc_hce.PatientARVPrescription')),
            ],
            options={
                'ordering': ['medication'],
            },
        ),
        migrations.CreateModel(
            name='PatientARVTreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observations', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(choices=[(b'Active', b'Active'), (b'Closed', b'Closed'), (b'Error', b'Error')], default=b'Active', max_length=8)),
                ('changeReason', models.CharField(choices=[(b'Toxicidad', b'Toxicidad'), (b'Abandono', b'Abandono'), (b'Simplificacion', b'Simplificacion'), (b'Fallo', b'Fallo')], max_length=20, null=True)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('medications', models.ManyToManyField(to='hc_masters.Medication')),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
            ],
            options={
                'ordering': ['state', '-startDate'],
            },
        ),
        migrations.CreateModel(
            name='PatientARVTreatmentMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityPerDay', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('quantityPerMonth', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('state', models.CharField(choices=[(b'Active', b'Active'), (b'Closed', b'Closed'), (b'Error', b'Error')], default=b'Active', max_length=8)),
                ('medication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_masters.Medication')),
                ('patientARVTreatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientARVTreatmentMedications', to='hc_hce.PatientARVTreatment')),
            ],
            options={
                'ordering': ['state', 'medication'],
            },
        ),
        migrations.CreateModel(
            name='PatientClinicalStudyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observations', models.CharField(max_length=2000, null=True)),
                ('state', models.CharField(choices=[(b'Active', b'Active'), (b'Error', b'Error')], default=b'Active', max_length=8)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('studyDate', models.DateField(blank=True, null=True)),
                ('clinicalStudy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_masters.ClinicalStudy')),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
            ],
            options={
                'ordering': ['state', '-studyDate', 'clinicalStudy__name'],
            },
        ),
        migrations.CreateModel(
            name='PatientFamilyHistoryProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(choices=[(b'Mother', b'Mother'), (b'Father', b'Father'), (b'Brother', b'Brother'), (b'Grandmother', b'Grandmother'), (b'Grandfather', b'Grandfather'), (b'Other', b'Other')], default=b'Other', max_length=15)),
                ('observations', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(choices=[(b'Active', b'Active'), (b'Error', b'Error')], default=b'Active', max_length=8)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_masters.Problem')),
            ],
            options={
                'ordering': ['state', 'problem__name'],
            },
        ),
        migrations.CreateModel(
            name='PatientMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityPerDay', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('quantityPerMonth', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('observations', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(choices=[(b'Active', b'Active'), (b'Closed', b'Closed'), (b'Error', b'Error')], default=b'Active', max_length=8)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_masters.Medication')),
                ('medicationPresentation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_masters.MedicationPresentation')),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
            ],
            options={
                'ordering': ['state', '-startDate', 'medication__name'],
            },
        ),
        migrations.CreateModel(
            name='PatientPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescripctionType', models.CharField(choices=[(b'Vaccine', b'Vaccine'), (b'Arv', b'Arv'), (b'Prophylaxis', b'Prophylaxis'), (b'General', b'General')], default=b'General', max_length=20)),
                ('observations', models.CharField(max_length=200, null=True)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('issuedDate', models.DateField()),
                ('duplicateRequired', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
            ],
            options={
                'ordering': ['-createdOn'],
            },
        ),
        migrations.CreateModel(
            name='PatientPrescriptionMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityPerDay', models.IntegerField(null=True)),
                ('quantityPerMonth', models.IntegerField(null=True)),
                ('patientMedication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_hce.PatientMedication')),
                ('prescription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescriptedMedications', to='hc_hce.PatientPrescription')),
            ],
            options={
                'ordering': ['patientMedication'],
            },
        ),
        migrations.CreateModel(
            name='PatientProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observations', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(choices=[(b'Active', b'Active'), (b'Closed', b'Closed'), (b'Error', b'Error')], default=b'Active', max_length=8)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('closeDate', models.DateField(blank=True, null=True)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_masters.Problem')),
            ],
            options={
                'ordering': ['state', '-startDate', 'problem__name'],
            },
        ),
        migrations.CreateModel(
            name='PatientVaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observations', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(choices=[(b'Applied', b'Applied'), (b'Error', b'Error')], default=b'Applied', max_length=8)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('appliedDate', models.DateField(blank=True, null=True)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_masters.Vaccine')),
            ],
            options={
                'ordering': ['state', 'vaccine__name', '-appliedDate'],
            },
        ),
        migrations.CreateModel(
            name='PatientVaccinePrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescripctionType', models.CharField(choices=[(b'Vaccine', b'Vaccine'), (b'Arv', b'Arv'), (b'Prophylaxis', b'Prophylaxis'), (b'General', b'General')], default=b'General', max_length=20)),
                ('observations', models.CharField(max_length=200, null=True)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('issuedDate', models.DateField()),
                ('duplicateRequired', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('paciente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
                ('prescriptedVaccines', models.ManyToManyField(to='hc_masters.Vaccine')),
            ],
            options={
                'ordering': ['-createdOn'],
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notaClinica', models.CharField(max_length=2000, null=True)),
                ('reason', models.CharField(max_length=200, null=True)),
                ('visitType', models.CharField(max_length=30, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('closed_on', models.DateTimeField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
                ('state', models.CharField(choices=[(b'Open', b'Open'), (b'Closed', b'Closed')], default=b'Open', max_length=8)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='VisitEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
                ('created_on', models.DateField(auto_now=True)),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='hc_hce.Visit')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='patientmedication',
            name='patientProblem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_hce.PatientProblem'),
        ),
        migrations.AddField(
            model_name='patientarvtreatment',
            name='patientProblem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_hce.PatientProblem'),
        ),
    ]
