#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_pacientes.models import Paciente
import reversion

@reversion.register()
class PhoneRegistry(ActiveModel):
    """
    Clase que representa un telefono de un paciente mínima necesaria para gestionar un Paciente
    """
    phoneNumber = models.CharField(max_length=14)
    observations = models.CharField(max_length=100, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='phones')
    updated_on = models.DateField(auto_now=True)
