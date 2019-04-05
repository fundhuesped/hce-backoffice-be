#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientPrescription
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.serializers import PatientPrescriptionMedicationNestSerializer
from hc_hce.serializers import PatientPrescriptionMedicationNestedSerializer

from hc_core.serializers import UserNestedSerializer


class PatientPrescriptionNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    prescriptedMedications = PatientPrescriptionMedicationNestSerializer(
        many=True,
        required=False
    )

    createdBy = UserNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        instance = PatientPrescription.objects.create(
            observations=validated_data.get('observations'),
            prescripctionType=validated_data.get('prescripctionType'),
            paciente=validated_data.get('paciente'),
            profesional=validated_data.get('profesional'),
            issuedDate=validated_data.get('issuedDate'),
            createdBy=validated_data.get('createdBy'),
            duplicateRequired=validated_data.get('duplicateRequired', False),
        )


        for prescriptedMedication in validated_data.get('prescriptedMedications'):
            prescriptedMedication['prescription'] = instance.id
            prescriptedMedication['patientMedication'] = prescriptedMedication['patientMedication'].id;
            serializer = PatientPrescriptionMedicationNestSerializer(data=prescriptedMedication)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return instance

    class Meta:
        model = PatientPrescription
        fields = ('id', 'paciente', 'createdBy', 'observations', 'createdOn', 'duplicateRequired', 'prescriptedMedications', 'issuedDate', 'prescripctionType', 'profesional')
