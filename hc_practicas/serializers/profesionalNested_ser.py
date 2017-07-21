#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from hc_practicas.models import Profesional
from hc_common.serializers import DocumentTypeNestedSerializer

class ProfesionalNestedSerializer(serializers.ModelSerializer):
    """
    Serializa un profesional, para ser incluida como objeto nested en otro objeto
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
    documentNumber=serializers.ReadOnlyField()
    email=serializers.ReadOnlyField()
    primaryPhoneNumber=serializers.ReadOnlyField()
    primaryPhoneContact=serializers.ReadOnlyField()
    primaryPhoneMessage=serializers.ReadOnlyField()

    url = serializers.HyperlinkedIdentityField(
        view_name='api:hc_practicas:Profesional-detail',
        lookup_field='pk'
    )

    def to_internal_value(self, data):
        if (isinstance(data, list) or isinstance(data, dict)):
            profesionales= Profesional.objects.filter(pk=data['id'])
        else:
            profesionales=Profesional.objects.filter(pk=data)

        if profesionales.count()>0:
            return profesionales[0]
        else:
            raise ValueError('Profesional not found')


    class Meta:
        model = Profesional
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'documentType', 'documentNumber', 'email','primaryPhoneNumber', 'primaryPhoneContact', 'primaryPhoneMessage', 'municipalNumber', 'licenseNumber','url', 'title')