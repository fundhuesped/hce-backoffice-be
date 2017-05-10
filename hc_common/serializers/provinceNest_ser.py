#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import Province


class ProvinceNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        province = Province.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            status=validated_data.get('status')
        )
        return province

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    class Meta:
        model = Province
        fields = ('id', 'name', 'description', 'status')
