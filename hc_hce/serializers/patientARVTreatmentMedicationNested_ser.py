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


class PatientARVTreatmentMedicationNestedSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    medication = MedicationNestedSerializer(
        many=False,
    )

    class Meta:
        model = PatientARVTreatmentMedication
        fields = ('id', 'medication', 'quantityPerDay', 'quantityPerMonth')
