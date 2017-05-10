#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import SocialService
from hc_common.serializers import TypeNestedSerializer


class SocialServiceNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:SocialService-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = SocialService
        fields = '__all__'
