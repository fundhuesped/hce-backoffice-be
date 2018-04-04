#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_masters.serializers import TypeNestedSerializer
from hc_laboratory.models import CategoriaDeterminacion


class CategoriaDeterminacionNestedSerializer(TypeNestedSerializer):


    class Meta(TypeNestedSerializer.Meta):
        model = CategoriaDeterminacion
        fields = '__all__'
