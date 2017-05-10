#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_masters.models import Problem


class ProblemNestedSerializer(TypeNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:Problem-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = Problem
        fields = '__all__'
