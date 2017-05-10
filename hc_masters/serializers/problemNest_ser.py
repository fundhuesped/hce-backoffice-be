#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.models import Problem


class ProblemNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        problem = Problem.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            status=validated_data.get('status'),
            problemType=validated_data.get('problemType')
        )
        return problem

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.problemType = validated_data.get('problemType', instance.problemType)
        instance.save()

        return instance

    class Meta:
        model = Problem
        fields = ('id', 'name', 'description', 'status', 'problemType')
