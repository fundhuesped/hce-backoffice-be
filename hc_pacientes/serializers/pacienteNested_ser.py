#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_pacientes.models import Paciente
from hc_common.serializers import DocumentTypeNestedSerializer
from hc_common.serializers import SocialServiceNestedSerializer

class PacienteNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un paciente, para ser incluida como objeto nested en otro objeto
    """

    id = serializers.IntegerField()
    firstName=serializers.ReadOnlyField()
    otherNames=serializers.ReadOnlyField()
    fatherSurname=serializers.ReadOnlyField()
    motherSurname=serializers.ReadOnlyField()
    birthDate=serializers.ReadOnlyField()
    documentType= DocumentTypeNestedSerializer(
        many=False,
        read_only=True
    )

    socialService= SocialServiceNestedSerializer(
        many=False,
        read_only=True
    )

    documentNumber=serializers.ReadOnlyField()
    email=serializers.ReadOnlyField()
    primaryPhoneNumber=serializers.ReadOnlyField()
    primaryPhoneContact=serializers.ReadOnlyField()
    primaryPhoneMessage=serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_pacientes:Paciente-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            pacientes= Paciente.objects.filter(pk=data['id'])
        else:
            pacientes=Paciente.objects.filter(pk=data)

        if pacientes.count()>0:
            return pacientes[0]
        else:
            raise ValueError('Paciente not found')

    class Meta:
        model = Paciente
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'documentType', 'documentNumber','genderAtBirth', 'email','primaryPhoneNumber', 'primaryPhoneContact', 'primaryPhoneMessage', 'url', 'socialService', 'socialServiceNumber', 'pns')