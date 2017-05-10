#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import Persona
import reversion

@reversion.register()
class Paciente(Persona):
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
    consent = models.CharField(max_length=14, choices=CONSENT_CHOICES, default=CONSENT_NA)
    updated_on = models.DateField(auto_now=True)
