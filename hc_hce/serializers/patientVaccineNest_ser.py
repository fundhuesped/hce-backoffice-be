#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientVaccine
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import VaccineNestedSerializer
from hc_core.serializers import UserNestedSerializer


class PatientVaccineNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    vaccine = VaccineNestedSerializer(
        many=False,
    )

    profesional = UserNestedSerializer(
        many=False,
    )

    def create(self, validated_data):

        patientVaccine = PatientVaccine.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientVaccine.STATE_APPLIED),
            paciente=validated_data.get('paciente'),
            profesional=validated_data.get('profesional'),
            vaccine=validated_data.get('vaccine'),
            appliedDate=validated_data.get('appliedDate'),
        )
        return patientVaccine

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):            
            instance.observations = validated_data.get('observations', instance.observations)
            instance.appliedDate = validated_data.get('appliedDate', instance.appliedDate)
            instance.save()
            return instance

        # Mark as error
        if validated_data.get('state') == PatientVaccine.STATE_ERROR:
            instance.state = PatientVaccine.STATE_ERROR
            instance.observations = validated_data.get('observations', instance.observations)
            instance.save()

        return instance


    class Meta:
        model = PatientVaccine
        fields = ('id', 'paciente', 'profesional', 'vaccine', 'observations', 'appliedDate', 'state')
