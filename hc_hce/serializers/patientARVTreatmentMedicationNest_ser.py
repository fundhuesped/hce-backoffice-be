#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientARVTreatmentMedication
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import MedicationNestedSerializer

from hc_core.serializers import UserNestedSerializer
from hc_core.serializers import UserNestedSerializer


class PatientARVTreatmentMedicationNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    medication = MedicationNestedSerializer(
        many=False,
    )
    profesional = UserNestedSerializer(
        many=False,
    )

    def create(self, validated_data):

        patientMedication = PatientARVTreatmentMedication.objects.create(
            patientARVTreatment=validated_data.get('patientARVTreatment'),
            quantityPerDay=validated_data.get('quantityPerDay'),
            profesional=validated_data.get('profesional'),
            quantityPerMonth=validated_data.get('quantityPerMonth'),
            medication=validated_data.get('medication')
        )
        return patientMedication

    class Meta:
        model = PatientARVTreatmentMedication
        fields = ('id', 'patientARVTreatment', 'profesional', 'medication', 'quantityPerDay', 'quantityPerMonth')
