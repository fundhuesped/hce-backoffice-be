#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from rest_framework import serializers
from hc_hce.models import Visit
from hc_hce.models import PatientMedication
from hc_hce.models import PatientARVTreatment
from hc_pacientes.models import Paciente

from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.serializers import PatientARVTreatmentMedicationNestSerializer
from hc_hce.serializers import PatientARVTreatmentMedicationNestedSerializer
from hc_hce.serializers import PatientProblemNestedSerializer
from rest_framework.exceptions import ValidationError

from hc_core.serializers import UserNestedSerializer


class PatientARVTreatmentNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    patientARVTreatmentMedications = PatientARVTreatmentMedicationNestedSerializer(
        many=True,
        required=False
    )

    patientProblem = PatientProblemNestedSerializer(
        many=False,
        required=False
    )

    def create(self, validated_data):

        instance = PatientARVTreatment.objects.create(
            observations=validated_data.get('observations'),
            state=validated_data.get('state', PatientARVTreatment.STATE_ACTIVE),
            paciente=validated_data.get('paciente'),
            patientProblem=validated_data.get('patientProblem'),
            startDate=validated_data.get('startDate'),
            endDate=validated_data.get('endDate'),
        )
        patientARVTreatmentMedications = validated_data.get('patientARVTreatmentMedications')
        for patientARVTreatmentMedication in patientARVTreatmentMedications:
            patientARVTreatmentMedication['patientARVTreatment'] = instance.id
            patientARVTreatmentMedication['medication'] = patientARVTreatmentMedication['medication'].id
            serializer = PatientARVTreatmentMedicationNestSerializer(data=patientARVTreatmentMedication)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return instance

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
        if validated_data.get('state') == PatientARVTreatment.STATE_ERROR:
            instance.state = PatientARVTreatment.STATE_ERROR
            instance.observations = validated_data.get('observations', instance.observations)
            instance.save()

        # Mark as error
        if validated_data.get('state') == PatientARVTreatment.STATE_CLOSED:
            if validated_data.get('changeReason') is not None: 
                instance.state = PatientARVTreatment.STATE_CLOSED
                instance.endDate = validated_data.get('endDate', instance.endDate)
                instance.changeReason = validated_data.get('changeReason')
                instance.observations = validated_data.get('observations', instance.observations)
                instance.save()
            else:
                raise ValidationError('Motivo de cambio es obligatorio')



        return instance


    class Meta:
        model = PatientARVTreatment
        fields = ('id', 'paciente', 'observations', 'startDate', 'patientARVTreatmentMedications','endDate', 'state', 'patientProblem', 'changeReason')
