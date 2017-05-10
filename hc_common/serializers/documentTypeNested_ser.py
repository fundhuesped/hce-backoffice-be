#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_common.models import DocumentType
from hc_common.serializers import TypeNestedSerializer


class DocumentTypeNestedSerializer(TypeNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_common:DocumentType-detail',
        lookup_field='pk'
    )

    class Meta(TypeNestedSerializer.Meta):
        model = DocumentType
        fields = '__all__'
