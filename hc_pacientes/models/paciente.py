#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import DocumentType
from hc_common.models import SexType
from hc_common.models import Location
from hc_common.models import SocialService
from hc_common.models import CivilStatusType
from hc_common.models import EducationType
from hc_common.models import Country
from hc_common.models import ActiveModel
import reversion

@reversion.register()
class Paciente(ActiveModel):
    """
    Clase que representa la información mínima necesaria para gestionar un Paciente
    """
    CONSENT_YES = 'Yes'
    CONSENT_NO = 'No'
    CONSENT_NA = 'Not asked'

    CONSENT_CHOICES = (
        (CONSENT_YES, 'Si'),
        (CONSENT_NO, 'No'),
        (CONSENT_NA, 'No preguntado')
    )

    idpaciente = models.CharField(max_length=20, null=True)
    prospect = models.BooleanField(default=False)
    # pns = models.CharField(max_length=20, null=True)
    consent = models.CharField(max_length=14, choices=CONSENT_CHOICES, default=CONSENT_NA)
    updated_on = models.DateField(auto_now=True)

    firstName = models.CharField(max_length=80, null=False, default="No informado")
    otherNames = models.CharField(max_length=80, null=True, blank=True)
    fatherSurname = models.CharField(max_length=80, null=False, default="No informado")
    motherSurname = models.CharField(max_length=40, null=True, blank=True)
    alias = models.CharField(max_length=80, null=True, blank=True)
    hceNumber = models.CharField(max_length=20, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    documentType = models.ForeignKey(DocumentType, null=True, blank=True, on_delete=models.SET_NULL)
    documentNumber = models.CharField(max_length=15, null=True, blank=True)
    genderAtBirth = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='pacienteGenderBirth', null=True, blank=True)
    genderOfChoice = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='pacienteGenderChoice', null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
    street = models.CharField(max_length=150, null=True, blank=True)
    postal = models.CharField(max_length=20, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='pacienteLocation', null=True, blank=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    socialService = models.ForeignKey(SocialService, models.SET_NULL, blank=True, null=True)
    socialServiceNumber = models.CharField(max_length=30, null=True, blank=True)
    civilStatus = models.ForeignKey(CivilStatusType, models.SET_NULL, blank=True, null=True)
    education = models.ForeignKey(EducationType, models.SET_NULL, blank=True, null=True)
    bornPlace = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    firstVisit = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    primaryPhoneNumber = models.CharField(max_length=20, null=True, blank=True)
    primaryPhoneContact = models.CharField(max_length=40, null=True, blank=True)
    primaryPhoneMessage = models.NullBooleanField(default=False, null=True, blank=True)
    secondPhoneNumber = models.CharField(max_length=20, blank=True, null=True)
    secondPhoneContact = models.CharField(max_length=40, blank=True, null=True)
    secondPhoneMessage = models.NullBooleanField(default=False, null=True, blank=True)
    thirdPhoneNumber = models.CharField(max_length=20, blank=True, null=True)
    thirdPhoneContact = models.CharField(max_length=40, blank=True, null=True)
    thirdPhoneMessage = models.NullBooleanField(default=False, null=True, blank=True)

    @property
    def pns(self):
        """
        Calculates the PNS code
        """
        if self.genderOfChoice.name == 'Masculino': 
            pns = 'M'
        else:
            pns = 'F'
        pns = pns + self.firstName[:2] + self.fatherSurname[:2] + self.birthDate.strftime('%d%m%Y')
        return pns.upper()

    class Meta:
        ordering = ['fatherSurname']