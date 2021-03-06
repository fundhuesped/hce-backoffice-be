#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_masters.models import Problem


class ProblemNestedSerializer(TypeNestedSerializer):

    class Meta(TypeNestedSerializer.Meta):
        model = Problem
        fields = '__all__'
