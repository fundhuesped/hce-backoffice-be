#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.serializers import TypeNestedSerializer, DistrictNestedSerializer
from hc_common.models import Location


class LocationNestedSerializer(TypeNestedSerializer):
    district = DistrictNestedSerializer(
        many=False,
        read_only=True
    )

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:Location-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = Location
        fields = ('id', 'name', 'description', 'status', 'district', 'url')
