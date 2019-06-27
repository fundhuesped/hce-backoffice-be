#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import DocumentType, SexType, Location, SocialService, CivilStatusType, EducationType, ActiveModel
import reversion

@reversion.register()
class Profesional(ActiveModel):
    """
    Clase que representa la información mínima necesaria para gestionar un Profesional (quien ejerce una prestación)
    """
    municipalNumber = models.CharField(max_length=8, null=False)
    licenseNumber = models.CharField(max_length=8, null=False)
    title = models.CharField(max_length=8, null=True)
    updated_on = models.DateField(auto_now=True)
    firstName = models.CharField(max_length=80, null=False, default="No informado")
    otherNames = models.CharField(max_length=80, null=True, blank=True)
    fatherSurname = models.CharField(max_length=80, null=False, default="No informado")
    motherSurname = models.CharField(max_length=40, null=True, blank=True)
    hceNumber = models.CharField(max_length=20, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    documentType = models.ForeignKey(DocumentType, null=True, blank=True, on_delete=models.SET_NULL)
    documentNumber = models.CharField(max_length=15, null=True, blank=True)
    genderAtBirth = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='profesionalGenderBirth', null=True, blank=True)
    genderOfChoice = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='profesionalGenderChoice', null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
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