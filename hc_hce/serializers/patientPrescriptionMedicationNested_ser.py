#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientPrescriptionMedication
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.serializers import PatientMedicationNestSerializer
from hc_hce.serializers import PatientMedicationNestedSerializer

from hc_core.serializers import UserNestedSerializer


class PatientPrescriptionMedicationNestedSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    patientMedication = PatientMedicationNestedSerializer(
        many=False,
    )

    def to_internal_value(self, data):
    	print data
        if (isinstance(data, list) or isinstance(data, dict)):
            medications= PatientPrescriptionMedication.objects.filter(pk=data['id'])
        else:
            medications=PatientPrescriptionMedication.objects.filter(pk=data)

        if medications.count()>0:
            return medications[0]
        else:
            raise ValueError('PatientPrescriptionMedication not found')

    class Meta:
        model = PatientPrescriptionMedication
        fields = ('id', 'patientMedication', 'quantityPerDay', 'quantityPerMonth')
