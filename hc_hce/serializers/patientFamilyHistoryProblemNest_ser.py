#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientFamilyHistoryProblem
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import ProblemNestedSerializer
from hc_core.serializers import UserNestedSerializer


class PatientFamilyHistoryProblemNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    problem = ProblemNestedSerializer(
        many=False,
    )

    def create(self, validated_data):

        patientFamilyHistoryProblem = PatientFamilyHistoryProblem.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientFamilyHistoryProblem.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            problem=validated_data.get('problem'),
            relationship=validated_data.get('relationship'),
        )
        return patientFamilyHistoryProblem

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):            
            instance.observations = validated_data.get('observations', instance.observations)
            instance.relationship = validated_data.get('relationship', instance.relationship)
            instance.save()
            return instance

        # Mark as error
        if validated_data.get('state') == PatientFamilyHistoryProblem.STATE_ERROR:
            instance.state = PatientFamilyHistoryProblem.STATE_ERROR
            instance.save()

        return instance


    class Meta:
        model = PatientFamilyHistoryProblem
        fields = ('id', 'paciente', 'problem', 'observations', 'relationship', 'createdOn', 'state')
