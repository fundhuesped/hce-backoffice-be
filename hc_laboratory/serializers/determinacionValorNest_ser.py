#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import transaction
from hc_laboratory.models import DeterminacionValor
from hc_laboratory.models import Determinacion
from hc_laboratory.serializers import DeterminacionNestedSerializer

from rest_framework import serializers


class DeterminacionValorNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    determinacion = DeterminacionNestedSerializer(
        many=False
    )

    @transaction.atomic
    def create(self, validated_data):

        instance = DeterminacionValor.objects.create(
            labResult=validated_data.get('labResult'),
            determinacion=validated_data.get('determinacion'),
            value=validated_data.get('value')
        )

        return instance


    class Meta:
        model = DeterminacionValor
        fields = ('id', 'determinacion', 'value', 'labResult')
