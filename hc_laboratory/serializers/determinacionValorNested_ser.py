#!/usr/bin/python
# -*- coding: utf-8 -*-

from hc_common.serializers import TypeNestedSerializer
from hc_laboratory.models import DeterminacionValor
from hc_laboratory.serializers import DeterminacionNestedSerializer

class DeterminacionValorNestedSerializer(TypeNestedSerializer):

    determinacion = DeterminacionNestedSerializer(
        many=False
    )

    
    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            if 'id' in data:
                mesa = DeterminacionValor.objects.filter(pk=data['id'])
            else:
                return data
        else:
            mesa=DeterminacionValor.objects.filter(pk=data)
        if mesa.count() > 0:
            return mesa[0]
        else:
            raise ValueError('DeterminacionValor not found')

    class Meta(TypeNestedSerializer.Meta):
        model = DeterminacionValor
        fields = ('id', 'determinacion', 'value')
