#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeNestedSerializer, ProvinceNestedSerializer
from hc_common.models import District


class DistrictNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:District-detail',
        lookup_field='pk'
    )
    province = ProvinceNestedSerializer(
        many=False,
        read_only=True
    )

    class Meta(TypeNestedSerializer.Meta):
        model = District
        fields = ('id', 'name', 'description', 'status', 'province', 'url')
