#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_hce.models import ProblemHivDetails

from hc_hce.serializers import PatientProblemNestSerializer



class ProblemHivDetailsNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    problem = PatientProblemNestSerializer(
        many=False,
    )

    def create(self, validated_data):

        problemHivDetails = ProblemHivDetails.objects.create(
            problem=validated_data.get('problem'),
            vertical=validated_data.get('vertical'),
            mujeres=validated_data.get('mujeres'),
            hombres=validated_data.get('hombres'),
            trans=validated_data.get('trans'),
            inyeccion=validated_data.get('inyeccion'),
            accidente=validated_data.get('accidente'),
            transfusion=validated_data.get('transfusion'),
            institucion=validated_data.get('institucion'),
            ciudad=validated_data.get('ciudad'),
            otra=validated_data.get('otra'),
            cual=validated_data.get('cual'),
            desconocida=validated_data.get('desconocida'),
            clinicalState=validated_data.get('clinicalState'),
            woman=validated_data.get('woman'),
        )
        return problemHivDetails

    class Meta:
        model = ProblemHivDetails
        fields = ('id', '', 'createdOn')
