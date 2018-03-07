#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_masters.models import MedicationPresentation


class MedicationPresentationNestedSerializer(TypeNestedSerializer):


    class Meta(TypeNestedSerializer.Meta):
        model = MedicationPresentation
        fields = '__all__'
