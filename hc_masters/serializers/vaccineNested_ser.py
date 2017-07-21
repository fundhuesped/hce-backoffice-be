#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_masters.models import Vaccine


class VaccineNestedSerializer(TypeNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_masters:Vaccine-details',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = Vaccine
        fields = '__all__'
