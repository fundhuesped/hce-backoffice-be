#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientARVPrescription
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.serializers import PatientARVPrescriptionMedicationNestSerializer

from hc_core.serializers import UserNestedSerializer


class PatientARVPrescriptionNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    prescriptedMedications = PatientARVPrescriptionMedicationNestSerializer(
        many=True,
        required=False
    )

    createdBy = UserNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        
        instance = PatientARVPrescription.objects.create(
            observations=validated_data.get('observations'),
            prescripctionType=validated_data.get('prescripctionType'),
            paciente=validated_data.get('paciente'),
            issuedDate=validated_data.get('issuedDate'),
            createdBy=validated_data.get('createdBy'), # Professional that created the prescription
            duplicateRequired=validated_data.get('duplicateRequired', False),
        )

        for prescriptedMedication in validated_data.get('prescriptedMedications'):

            prescriptedMedication['prescription'] = instance.id
            prescriptedMedication['medication'] = prescriptedMedication['medication'].id

            serializer = PatientARVPrescriptionMedicationNestSerializer(data=prescriptedMedication)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return instance

    class Meta:
        model = PatientARVPrescription
        fields = ('id', 'paciente', 'createdBy', 'observations', 'createdOn', 'duplicateRequired', 'prescriptedMedications', 'issuedDate', 'prescripctionType')
