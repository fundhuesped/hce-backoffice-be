#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import reversion

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

    profesional = UserNestedSerializer(
        many=False,
    )

    def create(self, validated_data):

        patientFamilyHistoryProblem = PatientFamilyHistoryProblem.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientFamilyHistoryProblem.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            profesional=validated_data.get('profesional'),
            problem=validated_data.get('problem'),
            relationship=validated_data.get('relationship'),
        )
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Family History Problem")       
        
        return patientFamilyHistoryProblem

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):  
            instance.problem = validated_data.get('problem');          
            instance.observations = validated_data.get('observations', instance.observations)
            instance.relationship = validated_data.get('relationship', instance.relationship)
            instance.save()
            return instance

        # Mark as error
        if validated_data.get('state') == PatientFamilyHistoryProblem.STATE_ERROR:
            instance.state = PatientFamilyHistoryProblem.STATE_ERROR
            instance.save()

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Family History Problem")       
        
        return instance


    class Meta:
        model = PatientFamilyHistoryProblem
        fields = ('id', 'paciente', 'profesional', 'problem', 'observations', 'relationship', 'createdOn', 'state')
