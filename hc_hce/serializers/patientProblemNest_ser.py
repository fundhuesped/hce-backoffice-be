#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import reversion

from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientProblem
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import ProblemNestedSerializer
from hc_core.serializers import UserNestedSerializer


class PatientProblemNestSerializer(serializers.ModelSerializer):
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

        patientProblem = PatientProblem.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientProblem.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            profesional=validated_data.get('profesional'),
            problem=validated_data.get('problem'),
            startDate=validated_data.get('startDate'),
            closeDate=validated_data.get('closeDate'),
            aditionalData=validated_data.get('aditionalData',None)
        )
        
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Patient Problem")       
       
        return patientProblem

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):         
            instance.problem = validated_data.get('problem')   
            instance.observations = validated_data.get('observations', instance.observations)
            instance.startDate = validated_data.get('startDate', instance.startDate)
            if instance.state == PatientProblem.STATE_CLOSED:
                instance.closeDate = validated_data.get('closeDate', instance.closeDate)

            instance.save()

            return instance

        # Close problem
        if instance.state == PatientProblem.STATE_ACTIVE and  validated_data.get('state') == PatientProblem.STATE_CLOSED:
            instance.problem = validated_data.get('problem')
            instance.observations = validated_data.get('observations', instance.observations)
            instance.state = PatientProblem.STATE_CLOSED
            closeDate = validated_data.get('closeDate')
            if closeDate is not None:
                instance.closeDate = closeDate
            instance.save()

            return instance

        # Mark as error
        if validated_data.get('state') == PatientProblem.STATE_ERROR:
            instance.state = PatientProblem.STATE_ERROR
            instance.save()

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Patient Problem")       
       
        return instance


    class Meta:
        model = PatientProblem
        fields = ('id', 'paciente', 'profesional', 'problem', 'observations', 'state', 'startDate', 'closeDate', 'createdOn', 'aditionalData')
