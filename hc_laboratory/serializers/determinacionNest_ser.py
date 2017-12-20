#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_laboratory.models import Determinacion


class DeterminacionNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        instance = Determinacion.objects.create(
            code=validated_data.get('code'),
            label=validated_data.get('label'),
            description=validated_data.get('description'),
            status=validated_data.get('status'),
        )
        return instance

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('code', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    class Meta:
        model = Determinacion
        fields = ('id', 'code', 'label', 'description', 'status')
