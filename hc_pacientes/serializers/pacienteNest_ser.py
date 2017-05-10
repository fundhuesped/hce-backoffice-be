#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion
from rest_framework import serializers
from hc_pacientes.models import Paciente
from hc_common.models import Persona
from hc_common.serializers import DocumentTypeNestedSerializer, SexTypeNestedSerializer, LocationNestedSerializer, \
    CivilStatusTypeNestedSerializer, SocialServiceNestedSerializer, EducationTypeNestedSerializer
from django.utils.translation import gettext as _

class PacienteNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    documentType = DocumentTypeNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )
    prospect = serializers.BooleanField(
        default=False,
        initial=False
    )
    status = serializers.CharField(
        max_length=8,
        initial=Persona.STATUS_ACTIVE,
        default=Persona.STATUS_ACTIVE
    )

    genderAtBirth = SexTypeNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    genderOfChoice = SexTypeNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    location = LocationNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    civilStatus = CivilStatusTypeNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    education = EducationTypeNestedSerializer(
        many=False,
        allow_null=True,
        required = False
    )

    socialService = SocialServiceNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    def validate(self, attrs):
        if (not 'primaryPhoneNumber' in attrs) or attrs['primaryPhoneNumber'] is None:
            raise serializers.ValidationError({'primaryPhoneNumber': _('El teléfono primario es obligatorio para un paciente')})

        if ('prospect' in attrs) and not attrs['prospect']:
            if (not 'primaryPhoneMessage' in attrs) or attrs['primaryPhoneMessage'] is None:
                raise serializers.ValidationError({'primaryPhoneMessage': _('El teléfono primario es obligatorio para un paciente')})
            if ((not 'documentNumber' in attrs) or attrs['documentNumber'] is None) or ((not 'documentType' in attrs) or attrs['documentType']) is None:
                raise serializers.ValidationError({'documentNumber': _('El tipo y número de documento son obligatorios')})
                
        return attrs

    def create(self, validated_data):
        try:
            documentType = validated_data.pop('documentType')
        except KeyError:
            documentType = None

        try:
            genderAtBirth = validated_data.pop('genderAtBirth')
        except KeyError:
            genderAtBirth = None

        try:
            genderOfChoice = validated_data.pop('genderOfChoice')
        except KeyError:
            genderOfChoice = None

        try:
            location = validated_data.pop('location')
        except KeyError:
            location = None

        try:
            civilStatus = validated_data.pop('civilStatus')
        except KeyError:
            civilStatus = None

        try:
            education = validated_data.pop('education')
        except KeyError:
            education = None

        try:
            socialService = validated_data.pop('socialService')
        except KeyError:
            socialService = None

        try:
            prospect = validated_data.pop('prospect')
        except KeyError:
            prospect = False

        paciente = Paciente.objects.create(
            idpaciente=validated_data.get('idpaciente'),
            prospect=prospect,
            firstName=validated_data.get('firstName'),
            otherNames=validated_data.get('otherNames'),
            fatherSurname=validated_data.get('fatherSurname'),
            motherSurname=validated_data.get('motherSurname'),
            birthDate=validated_data.get('birthDate'),
            consent=validated_data.get('consent', Paciente.CONSENT_NA),
            documentNumber=validated_data.get('documentNumber'),
            email=validated_data.get('email'),
            street=validated_data.get('street'),
            postal=validated_data.get('postal'),
            status=validated_data.get('status'),
            occupation=validated_data.get('occupation'),
            socialServiceNumber=validated_data.get('socialServiceNumber'),
            bornPlace=validated_data.get('bornPlace'),
            firstVisit=validated_data.get('firstVisit'),
            notes=validated_data.get('notes'),
            primaryPhoneNumber=validated_data.get('primaryPhoneNumber'),
            primaryPhoneContact=validated_data.get('primaryPhoneContact'),
            primaryPhoneMessage=validated_data.get('primaryPhoneMessage'),
            secondPhoneNumber=validated_data.get('secondPhoneNumber'),
            secondPhoneContact=validated_data.get('secondPhoneContact'),
            secondPhoneMessage=validated_data.get('secondPhoneMessage'),
            thirdPhoneNumber=validated_data.get('thirdPhoneNumber'),
            thirdPhoneContact=validated_data.get('thirdPhoneContact'),
            thirdPhoneMessage=validated_data.get('thirdPhoneMessage'),
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
            location=location,
            civilStatus=civilStatus,
            education=education,
            socialService=socialService
        )
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Paciente")
        return paciente

    def update(self, instance, validated_data):
        try:
            documentType = validated_data.pop('documentType')
        except KeyError:
            documentType = None

        try:
            genderAtBirth = validated_data.pop('genderAtBirth')
        except KeyError:
            genderAtBirth = None

        try:
            genderOfChoice = validated_data.pop('genderOfChoice')
        except KeyError:
            genderOfChoice = None

        try:
            location = validated_data.pop('location')
        except KeyError:
            location = None

        try:
            civilStatus = validated_data.pop('civilStatus')
        except KeyError:
            civilStatus = None

        try:
            education = validated_data.pop('education')
        except KeyError:
            education = None

        try:
            socialService = validated_data.pop('socialService')
        except KeyError:
            socialService = None

        instance.prospect = validated_data.get('prospect')
        instance.idpaciente = validated_data.get('idpaciente', instance.idpaciente)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.consent = validated_data.get('consent', instance.consent)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.street = validated_data.get('street', instance.street)
        instance.postal = validated_data.get('postal', instance.postal)
        instance.status=validated_data.get('status', instance.status)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.socialServiceNumber = validated_data.get('socialServiceNumber', instance.socialServiceNumber)
        instance.bornPlace = validated_data.get('bornPlace', instance.bornPlace)
        instance.firstVisit = validated_data.get('firstVisit', instance.firstVisit)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.primaryPhoneNumber = validated_data.get('primaryPhoneNumber', instance.primaryPhoneNumber)
        instance.primaryPhoneContact = validated_data.get('primaryPhoneContact', instance.primaryPhoneContact)
        instance.primaryPhoneMessage = validated_data.get('primaryPhoneMessage', instance.primaryPhoneMessage)
        instance.secondPhoneNumber = validated_data.get('secondPhoneNumber', instance.secondPhoneNumber)
        instance.secondPhoneContact = validated_data.get('secondPhoneContact', instance.secondPhoneContact)
        instance.secondPhoneMessage = validated_data.get('secondPhoneMessage', instance.secondPhoneMessage)
        instance.thirdPhoneNumber = validated_data.get('thirdPhoneNumber', instance.thirdPhoneNumber)
        instance.thirdPhoneContact = validated_data.get('thirdPhoneContact', instance.thirdPhoneContact)
        instance.thirdPhoneMessage = validated_data.get('thirdPhoneMessage', instance.thirdPhoneMessage)
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.genderOfChoice = genderOfChoice
        instance.location = location
        instance.civilStatus = civilStatus
        instance.education = education
        instance.socialService = socialService
        instance.save()

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Paciente")
        return instance

    class Meta:
        model = Paciente
        fields = ('id', 'idpaciente', 'prospect', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email',
                  'street', 'postal', 'status', 'consent','documentType', 'documentNumber', 'genderAtBirth',
                  'genderOfChoice', 'location', 'occupation', 'civilStatus', 'education', 'socialService',
                  'socialServiceNumber', 'bornPlace', 'firstVisit', 'notes', 'primaryPhoneNumber',
                  'primaryPhoneContact', 'primaryPhoneMessage', 'secondPhoneNumber', 'secondPhoneContact',
                  'secondPhoneMessage', 'thirdPhoneNumber', 'thirdPhoneContact', 'thirdPhoneMessage')
