#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientPrescription
from hc_hce.models import PatientPrescriptionMedication
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.serializers import PatientMedicationNestedSerializer
from hc_hce.serializers import PatientMedicationNestSerializer

from hc_core.serializers import UserNestedSerializer


class PatientPrescriptionMedicationNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    patientMedication = PatientMedicationNestedSerializer(
        many=False,
    )

    def create(self, validated_data):
        instance = PatientPrescriptionMedication.objects.create(
            prescription=validated_data.get('prescription'),
            patientMedication=validated_data.get('patientMedication'),
            quantityPerDay=validated_data.get('quantityPerDay'),
            quantityPerMonth=validated_data.get('quantityPerMonth')
        )

        return instance

    class Meta:
        model = PatientPrescriptionMedication
        fields = ('id', 'prescription', 'patientMedication', 'quantityPerDay', 'quantityPerMonth')
