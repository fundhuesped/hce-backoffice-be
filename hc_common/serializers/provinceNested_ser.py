#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeNestedSerializer
from hc_common.models import Province


class ProvinceNestedSerializer(TypeNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:Province-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = Province
        fields = '__all__'
