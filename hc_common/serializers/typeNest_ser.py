#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers


class TypeNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    def create(self, validated_data):
        custom = self.Meta.model.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            status=validated_data.get('status')
        )

        return custom

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    class Meta:
        fields = ('id', 'name', 'description', 'status')
