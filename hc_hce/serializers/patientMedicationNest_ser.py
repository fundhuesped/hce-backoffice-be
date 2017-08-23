#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientMedication
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import MedicationNestedSerializer
from hc_hce.serializers import PatientProblemNestedSerializer

from hc_core.serializers import UserNestedSerializer


class PatientMedicationNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    medication = MedicationNestedSerializer(
        many=False,
    )

    patientProblem = PatientProblemNestedSerializer(
        many=False,
        required=False
    )

    def create(self, validated_data):

        patientMedication = PatientMedication.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientMedication.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            patientProblem=validated_data.get('patientProblem'),
            medication=validated_data.get('medication'),
            startDate=validated_data.get('startDate'),
            endDate=validated_data.get('endDate'),
        )
        return patientMedication

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):            
            instance.observations = validated_data.get('observations', instance.observations)
            instance.startDate = validated_data.get('startDate', instance.startDate)
            instance.endDate = validated_data.get('endDate', instance.endDate)
            instance.patientProblem = validated_data.get('patientProblem', instance.patientProblem)

            instance.save()
            return instance

        # Mark as error
        if validated_data.get('state') == PatientMedication.STATE_ERROR:
            instance.state = PatientMedication.STATE_ERROR
            instance.observations = validated_data.get('observations', instance.observations)
            instance.save()

        return instance


    class Meta:
        model = PatientMedication
        fields = ('id', 'paciente', 'medication', 'observations', 'startDate', 'endDate', 'state', 'patientProblem')
