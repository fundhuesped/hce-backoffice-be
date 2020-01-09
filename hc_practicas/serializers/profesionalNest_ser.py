#!/usr/bin/python
# -*- coding: utf-8 -*-

import reversion
import datetime as dt
import copy
from django.utils.translation import gettext as _
from hc_common.models import Location
from hc_common.serializers import CivilStatusTypeNestedSerializer
from hc_common.serializers import DocumentTypeNestedSerializer
from hc_common.serializers import EducationTypeNestedSerializer
from hc_common.serializers import LocationNestedSerializer
from hc_common.serializers import SexTypeNestedSerializer
from hc_common.serializers import SocialServiceNestedSerializer
from hc_common.serializers import ProtocolNestedSerializer
from hc_practicas.models import Profesional
from rest_framework import serializers


class ProfesionalNestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    status = serializers.CharField(
        default=Profesional.STATUS_ACTIVE
    )

    documentType = DocumentTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    education = EducationTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    socialService = SocialServiceNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    genderAtBirth = SexTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )
    
    protocol = ProtocolNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    genderOfChoice = SexTypeNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    location = LocationNestedSerializer(
        many=False,
        required=False,
        allow_null=True
    )

    civilStatus = CivilStatusTypeNestedSerializer(
        many=False,
        allow_null=True,
        required=False
    )

    def validate(self, attrs):
        """
        Validaciones de datos básicos para el alta de un profesional
        :param attrs:
        :return:
        """

        #HUES-215: Solo son obligatorios nombre y apellido
        """
        if (not 'primaryPhoneNumber' in attrs) or attrs['primaryPhoneNumber'] is None:
            raise serializers.ValidationError({'primaryPhoneNumber': _('El teléfono primario es obligatorio para un profesional')})
        if (not 'primaryPhoneContact' in attrs) or attrs['primaryPhoneContact'] is None:
            raise serializers.ValidationError({'primaryPhoneContact': _('El teléfono primario es obligatorio para un profesional')})
        if (not 'primaryPhoneMessage' in attrs) or attrs['primaryPhoneMessage'] is None:
            raise serializers.ValidationError({'primaryPhoneMessage': _('El teléfono primario es obligatorio para un profesional')})
        if (not 'birthDate' in attrs) or attrs['birthDate'] is None:
           raise serializers.ValidationError({'birthDate': _('La fecha de nacimiento es obligatoria para un profesional')})
        if ((not 'documentNumber' in attrs) or attrs['documentNumber'] is None) or ((not 'documentType' in attrs) or attrs['documentType']) is None:
            raise serializers.ValidationError({'documentNumber': _('El tipo y número de documento son obligatorios')})
        if (not 'genderAtBirth' in attrs) or attrs['genderAtBirth'] is None:
            raise serializers.ValidationError({'genderAtBirth': _('El sexo al nacer es obligatorio')})
        if  (not 'genderOfChoice' in attrs) or attrs['genderOfChoice'] is None:
            raise serializers.ValidationError({'genderOfChoice': _('El sexo por elección es obligatorio')})
        if (not 'street' in attrs) or attrs['street'] is None:
            raise serializers.ValidationError({'street': _('El domicilio es obligatorio')})
        if (not 'postal' in attrs) or attrs['postal'] is None:
            raise serializers.ValidationError({'postal': _('El código postal es obligatorio')})
        if (not 'location' in attrs) or attrs['location'] is None:
            raise serializers.ValidationError({'location': _('La provincia, partido y localidad son obligatorios')})
        """

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
            protocol = validated_data.pop('protocol')
        except KeyError:
            protocol = None

        try:
            genderOfChoice = validated_data.pop('genderOfChoice')
        except KeyError:
            genderOfChoice = None

        try:
            location = validated_data.pop('location')
        except KeyError:
            location = None

        try:
            socialService = validated_data.pop('socialService')
        except KeyError:
            socialService = None

        try:
            civilStatus = validated_data.pop('civilStatus')
        except KeyError:
            civilStatus = None

        try:
            education = validated_data.pop('education')
        except KeyError:
            education = None


        profesional = Profesional.objects.create(
            firstName=validated_data.get('firstName'),
            otherNames=validated_data.get('otherNames'),
            fatherSurname=validated_data.get('fatherSurname'),
            motherSurname=validated_data.get('motherSurname'),
            municipalNumber=validated_data.get('municipalNumber'),
            licenseNumber=validated_data.get('licenseNumber'),
            birthDate=validated_data.get('birthDate'),
            documentNumber=validated_data.get('documentNumber'),
            email=validated_data.get('email'),
            street=validated_data.get('street'),
            postal=validated_data.get('postal'),
            status=validated_data.get('status'),
            notes=validated_data.get('notes'),
            primaryPhoneNumber=validated_data.get('primaryPhoneNumber'),
            primaryPhoneContact=validated_data.get('primaryPhoneContact'),
            primaryPhoneMessage=validated_data.get('primaryPhoneMessage'),
            socialServiceNumber=validated_data.get('socialServiceNumber'),
            bornPlace = validated_data.get('bornPlace'),
            occupation=validated_data.get('occupation'),
            title=validated_data.get('title'),
            education=education,
            documentType=documentType,
            genderAtBirth=genderAtBirth,
            genderOfChoice=genderOfChoice,
            protocol=protocol,
            socialService=socialService,
            location=location,
            civilStatus=civilStatus,
        )

        profesional.save()
        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Created Profesional")

        return profesional

    def update(self, instance, validated_data):
        documentType = validated_data.pop('documentType')
        genderAtBirth = validated_data.pop('genderAtBirth')
        genderOfChoice = validated_data.pop('genderOfChoice')
        protocol = validated_data.pop('protocol')
        location = validated_data.pop('location')
        civilStatus = validated_data.pop('civilStatus')
        socialService = validated_data.pop('socialService')
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.otherNames = validated_data.get('otherNames', instance.otherNames)
        instance.fatherSurname = validated_data.get('fatherSurname', instance.fatherSurname)
        instance.motherSurname = validated_data.get('motherSurname', instance.motherSurname)
        instance.municipalNumber = validated_data.get('municipalNumber', instance.municipalNumber)
        instance.licenseNumber = validated_data.get('licenseNumber', instance.licenseNumber)
        instance.birthDate = validated_data.get('birthDate', instance.birthDate)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.bornPlace = validated_data.get('bornPlace', instance.bornPlace)
        instance.email = validated_data.get('email', instance.email)
        instance.street = validated_data.get('street', instance.street)
        instance.postal = validated_data.get('postal', instance.postal)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.title = validated_data.get('title')
        instance.education = validated_data.get('education', instance.education)
        instance.primaryPhoneNumber = validated_data.get('primaryPhoneNumber', instance.primaryPhoneNumber)
        instance.primaryPhoneContact = validated_data.get('primaryPhoneContact', instance.primaryPhoneContact)
        instance.primaryPhoneMessage = validated_data.get('primaryPhoneMessage', instance.primaryPhoneMessage)
        instance.socialServiceNumber = validated_data.get('socialServiceNumber', instance.socialServiceNumber)
        instance.socialService = socialService
        instance.documentType = documentType
        instance.genderAtBirth = genderAtBirth
        instance.protocol = protocol
        instance.genderOfChoice = genderOfChoice
        instance.location = location
        instance.civilStatus = civilStatus
        status = validated_data.get('status', instance.status)

        # Agrego datos de la revision
        reversion.set_user(self._context['request'].user)
        reversion.set_comment("Modified Profesional")

        if instance.status != status:

            if instance.status == Profesional.STATUS_ACTIVE and status == Profesional.STATUS_INACTIVE:
                instance.status = Profesional.STATUS_INACTIVE
                # Agrego datos de la revision
                reversion.set_comment("Deactivated Profesional")

            elif instance.status == Profesional.STATUS_INACTIVE and status == Profesional.STATUS_ACTIVE:
                instance.status = Profesional.STATUS_ACTIVE
                # Agrego datos de la revision
                reversion.set_comment("Activated Profesional")


        instance.save()
        return instance

    class Meta:
        model = Profesional
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }
        fields = ('id', 'firstName', 'otherNames', 'fatherSurname', 'motherSurname', 'birthDate', 'email', 'street', 'postal', 'status', 'documentType', 'documentNumber', 'genderAtBirth', 'genderOfChoice', 'protocol', 'location', 'bornPlace', 'occupation', 'education', 'civilStatus', 'notes', 'primaryPhoneNumber', 'primaryPhoneContact', 'primaryPhoneMessage', 'socialService', 'socialServiceNumber', 'municipalNumber', 'licenseNumber', 'title')
