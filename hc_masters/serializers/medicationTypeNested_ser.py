#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_masters.models import MedicationType


class MedicationTypeNestedSerializer(TypeNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:MedicationType-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = MedicationType
        fields = '__all__'
