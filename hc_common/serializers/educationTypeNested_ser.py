#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import EducationType
from hc_common.serializers import TypeNestedSerializer


class EducationTypeNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:EducationType-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = EducationType
        fields = '__all__'
