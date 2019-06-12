#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Vaccine
from django.contrib.auth.models import User
import reversion

@reversion.register()
class PatientVaccine(models.Model):
    """
    Clase que representa un problema de un paciente
    """

    STATE_APPLIED = 'Applied'
    STATE_ERROR = 'Error'

    STATE_CHOICES = (
        (STATE_APPLIED, 'Applied'),
        (STATE_ERROR, 'Error')
    )

    observations = models.CharField(max_length=200, null=True)
    paciente = models.ForeignKey(Paciente,blank=True, null=False, on_delete=models.SET_NULL)
    vaccine = models.ForeignKey(Vaccine, null=False, on_delete=models.CASCADE)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_APPLIED)
    profesional = models.ForeignKey(User, null=False, on_delete=models.SET_NULL)
    createdOn = models.DateTimeField(auto_now=True)
    appliedDate = models.DateField(blank=True, null=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state', '-appliedDate']
