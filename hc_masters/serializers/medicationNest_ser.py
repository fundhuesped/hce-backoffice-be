#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.models import Medication
from hc_masters.serializers import MedicationTypeNestSerializer
from hc_masters.serializers import MedicationPresentationNestedSerializer


class MedicationNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    medicationType = MedicationTypeNestSerializer(
        many=False
    )
    presentations = MedicationPresentationNestedSerializer(
        many=True
    )

    def create(self, validated_data):
        medication = Medication.objects.create(
            name=validated_data.get('name'),
            composition=validated_data.get('composition'),
            status=validated_data.get('status'),
            medicationType=validated_data.get('medicationType'),
            abbreviation=validated_data.get('abbreviation'),

        )
        return medication

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.composition = validated_data.get('composition', instance.composition)
        instance.status = validated_data.get('status', instance.status)
        instance.medicationType = validated_data.get('medicationType', instance.medicationType)
        instance.abbreviation = validated_data.get('abbreviation', instance.abbreviation)
        instance.save()

        return instance

    class Meta:
        model = Medication
        fields = ('id', 'name', 'composition', 'status', 'medicationType', 'presentations', 'abbreviation', 'presentation')
