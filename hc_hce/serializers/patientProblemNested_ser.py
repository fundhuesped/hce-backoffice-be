#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_hce.serializers import ProblemNestedSerializer
from hc_pacientes.serializers import PacienteNestedSerializer
from hc_hce.models import PatientProblem


class PatientProblemNestedSerializer(TypeNestedSerializer):
    problem = ProblemNestedSerializer(
        many=False,
    )

    paciente = PacienteNestedSerializer(
        many=False,
    )
    
    class Meta(TypeNestedSerializer.Meta):
        model = PatientProblem
        fields = '__all__'
