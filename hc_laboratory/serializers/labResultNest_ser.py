#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from django.db import transaction
from hc_laboratory.models import LabResult
from hc_laboratory.serializers import DeterminacionValorNestedSerializer
from hc_laboratory.serializers import DeterminacionValorNestSerializer
from hc_pacientes.serializers import PacienteNestedSerializer
from rest_framework import serializers


class LabResultNestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    paciente = PacienteNestedSerializer(
        many=False
    )

    values = DeterminacionValorNestedSerializer(
        many=True
    )

    @transaction.atomic
    def create(self, validated_data):

        instance = LabResult.objects.create(
            paciente=validated_data.get('paciente'),
            date=validated_data.get('date')
        )
        instance.save()
        for value in validated_data.get('values'):
            value['labResult'] = instance.id
            serializer = DeterminacionValorNestSerializer(data=value)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return instance

    class Meta:
        model = LabResult
        fields = ('id', 'date', 'values', 'paciente','status', 'createdOn', 'modifiedOn')
