#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Protocol
from hc_common.serializers import TypeNestedSerializer


class ProtocolNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:Protocol-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = Protocol
        fields = '__all__'
