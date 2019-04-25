#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion

from rest_framework import serializers
from hc_hce.models import Visit
from hc_pacientes.models import Paciente
from hc_pacientes.serializers import PacienteNestedSerializer
from hc_core.serializers import UserNestedSerializer


class VisitNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    paciente = PacienteNestedSerializer(
        many=False,
    )

    profesional = UserNestedSerializer(
        many=False,
    )

    def create(self, validated_data):

        visit = Visit.objects.create(
            profesional=validated_data.get('profesional'),
            notaClinica=validated_data.get('notaClinica'),
            paciente=validated_data.get('paciente'),
            reason=validated_data.get('reason'),
            visitType=validated_data.get('visitType')
        )

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Visit")       
       
        return visit

    def update(self, instance, validated_data):
        instance.notaClinica = validated_data.get('notaClinica', instance.notaClinica)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.visitType = validated_data.get('visitType', instance.visitType)
        instance.status = validated_data.get('status', instance.visitType)

        if instance.state == Visit.STATE_OPEN and  validated_data.get('state') == Visit.STATE_CLOSED:
            instance.state = validated_data.get('state')
        else:
            if(validated_data.get('state') == Visit.STATE_CANCELED):
                instance.state = validated_data.get('state')
        instance.save()

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Visit")       
       
        return instance

    class Meta:
        model = Visit
        fields = ('id', 'profesional', 'paciente', 'notaClinica', 'status', 'state', 'date', 'reason', 'visitType', 'created_on')
