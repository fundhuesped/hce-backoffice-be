#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
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

    def create(self, validated_data):

        patientProblem = PatientProblem.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientProblem.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            problem=validated_data.get('problem'),
            startDate=validated_data.get('startDate'),
            closeDate=validated_data.get('closeDate')
        )
        return patientProblem

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):            
            instance.observations = validated_data.get('observations', instance.observations),
            instance.startDate = validated_data.get('startDate', instance.startDate),
            if instance.state == PatientProblem.STATE_CLOSED:
                instance.closeDate = validated_data.get('closeDate', instance.closeDate)

            instance.save()

            return instance

        # Close problem
        if instance.state == PatientProblem.STATE_ACTIVE and  validated_data.get('state') == PatientProblem.STATE_CLOSED:
            instance.state = PatientProblem.STATE_CLOSED
            closeDate = validated_data.get('closeDate')
            # if closeDate is None:
            #     instance.closeDate = closeDate
            instance.save()

            return instance

        # Mark as error
        if validated_data.get('state') == PatientProblem.STATE_ERROR:
            instance.state = PatientProblem.STATE_ERROR
            instance.save()

        return instance


    class Meta:
        model = PatientProblem
        fields = ('id', 'paciente', 'problem', 'observations', 'state', 'startDate', 'closeDate', 'createdOn')
