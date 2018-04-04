#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.models import ClinicalStudy


class ClinicalStudyNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        vaccine = ClinicalStudy.objects.create(
            name=validated_data.get('name'),
            status=validated_data.get('status'),
        )
        return vaccine

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    class Meta:
        model = ClinicalStudy
        fields = ('id', 'name', 'status', 'synonym')
