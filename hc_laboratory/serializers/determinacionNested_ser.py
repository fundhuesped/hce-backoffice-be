#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_laboratory.models import Determinacion


class DeterminacionNestedSerializer(TypeNestedSerializer):


    class Meta(TypeNestedSerializer.Meta):
        model = Determinacion
        fields = '__all__'
