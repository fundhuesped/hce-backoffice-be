#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import PatientMedication
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.serializers import PatientMedicationNestSerializer
from hc_hce.serializers import PatientProblemNestedSerializer
from hc_masters.serializers import MedicationNestedSerializer
from hc_hce.serializers import MedicationPresentationNestedSerializer

from hc_core.serializers import UserNestedSerializer


class PatientMedicationNestedSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    medication = MedicationNestedSerializer(
        many=False
    )
    patientProblem = PatientProblemNestedSerializer(
        many=False,
        required=False
    )
    medicationPresentation = MedicationPresentationNestedSerializer(
        many=False,
        required=False
    )

    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            medications= PatientMedication.objects.filter(pk=data['id'])
        else:
            medications=PatientMedication.objects.filter(pk=data)

        if medications.count()>0:
            return medications[0]
        else:
            raise ValueError('PatientMedication not found')

    class Meta:
        model = PatientMedication
        fields = ('id', 'medication', 'observations', 'startDate', 'endDate', 'state', 'patientProblem', 'medicationPresentation')
