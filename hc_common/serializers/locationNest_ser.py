#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Location, District
from hc_common.serializers import DistrictNestedSerializer


class LocationNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    district = DistrictNestedSerializer(
        many=False
    )

    def create(self, validated_data):
        district = validated_data.pop('district')
        location = Location.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            status=validated_data.get('status'),
            district=district
        )
        return location

    def update(self, instance, validated_data):
        district = validated_data.pop('district')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.district = district
        instance.save()

        return instance

    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'status', 'district')
        
