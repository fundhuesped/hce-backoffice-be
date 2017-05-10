#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import SexType
from hc_common.serializers import TypeNestedSerializer


class SexTypeNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:SexType-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = SexType
        fields = '__all__'
