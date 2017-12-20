#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientPrescription
from hc_hce.models import PatientPrescriptionMedication
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import MedicationNestedSerializer

from hc_core.serializers import UserNestedSerializer


class PatientPrescriptionMedicationNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    medication = MedicationNestedSerializer(
        many=False,
    )

    def create(self, validated_data):
        instance = PatientPrescriptionMedication.objects.create(
            prescription=validated_data.get('prescription'),
            medication=validated_data.get('medication'),
            quantityPerDay=validated_data.get('quantityPerDay'),
            quantityPerMonth=validated_data.get('quantityPerMonth')
        )

        return instance

    class Meta:
        model = PatientPrescriptionMedication
        fields = ('id', 'prescription', 'medication', 'quantityPerDay', 'quantityPerMonth')
