#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import CivilStatusType
from hc_common.serializers import TypeNestedSerializer


class CivilStatusTypeNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:CivilStatusType-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = CivilStatusType
        fields = '__all__'


