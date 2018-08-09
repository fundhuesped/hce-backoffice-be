#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientVaccinePrescription
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import VaccineNestedSerializer

from hc_core.serializers import UserNestedSerializer


class PatientVaccinePrescriptionNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    prescriptedVaccines = VaccineNestedSerializer(
        many=True,
        required=False
    )

    createdBy = UserNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        instance = PatientVaccinePrescription.objects.create(
            observations=validated_data.get('observations'),
            prescripctionType=validated_data.get('prescripctionType'),
            paciente=validated_data.get('paciente'),
            issuedDate=validated_data.get('issuedDate'),
            createdBy=validated_data.get('createdBy'),
            duplicateRequired=validated_data.get('duplicateRequired', False),
        )


        for prescriptedVaccine in validated_data.get('prescriptedVaccines'):
            instance.prescriptedVaccines.add(prescriptedVaccine)

        return instance

    class Meta:
        model = PatientVaccinePrescription
        fields = ('id', 'paciente', 'createdBy', 'observations', 'createdOn', 'duplicateRequired', 'prescriptedVaccines', 'issuedDate', 'prescripctionType')
