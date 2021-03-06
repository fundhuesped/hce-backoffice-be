#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import reversion

from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientMedication
from hc_pacientes.models import Paciente
from hc_hce.models import PatientProblem

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import MedicationNestedSerializer
from hc_masters.serializers import MedicationPresentationNestedSerializer
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
        required=False,
        allow_null=True
    )

    medicationPresentation = MedicationPresentationNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    profesional = UserNestedSerializer(
        many=False,
    )


    def create(self, validated_data):

        patientMedication = PatientMedication.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientMedication.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            patientProblem=validated_data.get('patientProblem'),
            profesional=validated_data.get('profesional'),
            quantityPerMonth=validated_data.get('quantityPerMonth'),
            quantityPerDay=validated_data.get('quantityPerDay'),
            medication=validated_data.get('medication'),
            medicationPresentation=validated_data.get('medicationPresentation'),
            startDate=validated_data.get('startDate'),
            endDate=validated_data.get('endDate'),
        )
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Patient Medication")       
       
        return patientMedication

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state != PatientMedication.STATE_ERROR:
            instance.startDate = validated_data.get('startDate', instance.startDate)
            instance.endDate = validated_data.get('endDate', instance.endDate)
            instance.state = validated_data.get('state', instance.state)
            instance.quantityPerMonth = validated_data.get('quantityPerMonth', instance.quantityPerMonth)
            instance.quantityPerDay = validated_data.get('quantityPerDay', instance.quantityPerDay)
            instance.patientProblem = validated_data.get('patientProblem', instance.patientProblem)
            instance.observations = validated_data.get('observations', instance.observations)
            instance.save()
            return instance

        if instance.state == PatientMedication.STATE_ERROR:
            instance.observations = validated_data.get('observations', instance.observations)
            instance.save()
            return instance

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Patient Medication")       
       
        return instance


    class Meta:
        model = PatientMedication
        fields = ('id', 'paciente', 'profesional', 'medication',  'quantityPerMonth', 'quantityPerDay', 'observations', 'startDate', 'endDate', 'state', 'patientProblem', 'medicationPresentation', 'createdOn')
