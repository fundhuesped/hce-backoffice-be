#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import DocumentType, SexType, Location, SocialService, CivilStatusType, EducationType, ActiveModel


class Persona(ActiveModel):
    """
    Clase que representa la información mínima necesaria para gestionar un Documento
    """
    firstName = models.CharField(max_length=80, null=False)
    otherNames = models.CharField(max_length=80, null=True, blank=True)
    fatherSurname = models.CharField(max_length=80, null=False)
    motherSurname = models.CharField(max_length=40, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    documentType = models.ForeignKey(DocumentType, null=True, blank=True)
    documentNumber = models.CharField(max_length=15, null=True, blank=True)
    genderAtBirth = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='personGenderBirth', null=True, blank=True)
    genderOfChoice = models.ForeignKey(SexType, on_delete=models.CASCADE, related_name='personGenderChoice', null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=8, choices=ActiveModel.STATUS_CHOICES, default=ActiveModel.STATUS_ACTIVE)
    street = models.CharField(max_length=150, null=True, blank=True)
    postal = models.CharField(max_length=20, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='personLocation', null=True, blank=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    socialService = models.ForeignKey(SocialService, models.SET_NULL, blank=True, null=True)
    socialServiceNumber = models.CharField(max_length=30, null=True, blank=True)
    civilStatus = models.ForeignKey(CivilStatusType, models.SET_NULL, blank=True, null=True)
    education = models.ForeignKey(EducationType, models.SET_NULL, blank=True, null=True)
    bornPlace = models.CharField(max_length=50, null=True, blank=True)
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

    class Meta:
        ordering = ['fatherSurname']