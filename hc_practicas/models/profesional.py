#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import Persona
import reversion

@reversion.register()
class Profesional(Persona):
    """
    Clase que representa la información mínima necesaria para gestionar un Profesional (quien ejerce una prestación)
    """
    municipalNumber = models.CharField(max_length=8, null=False)
    licenseNumber = models.CharField(max_length=8, null=False)
    title = models.CharField(max_length=8, null=True)
    updated_on = models.DateField(auto_now=True)
