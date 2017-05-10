#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_masters.models import Medication


class MedicationNestedSerializer(TypeNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:Medication-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            medications= Medication.objects.filter(pk=data['id'])
        else:
            medications=Medication.objects.filter(pk=data)

        if medications.count()>0:
            return medications[0]
        else:
            raise ValueError('Medication not found')

    class Meta(TypeNestedSerializer.Meta):
        model = Medication
        fields = '__all__'
