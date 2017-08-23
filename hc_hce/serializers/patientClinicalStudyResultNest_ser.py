#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientClinicalStudyResult
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_masters.serializers import ClinicalStudyNestedSerializer
from hc_core.serializers import UserNestedSerializer


class PatientClinicalStudyResultNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    clinicalStudy = ClinicalStudyNestedSerializer(
        many=False,
    )

    def create(self, validated_data):

        patientClinicalStudyResult = PatientClinicalStudyResult.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientClinicalStudyResult.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            clinicalStudy=validated_data.get('clinicalStudy'),
            studyDate=validated_data.get('studyDate'),
        )
        return patientClinicalStudyResult

    def update(self, instance, validated_data):

        # Edit problem
        if instance.state == validated_data.get('state'):            
            instance.observations = validated_data.get('observations', instance.observations)
            instance.studyDate = validated_data.get('studyDate', instance.studyDate)
            instance.save()
            return instance

        # Mark as error
        if validated_data.get('state') == PatientClinicalStudyResult.STATE_ERROR:
            instance.state = PatientClinicalStudyResult.STATE_ERROR
            instance.observations = validated_data.get('observations', instance.observations)
            instance.save()

        return instance


    class Meta:
        model = PatientClinicalStudyResult
        fields = ('id', 'paciente', 'clinicalStudy', 'observations', 'studyDate', 'state')
