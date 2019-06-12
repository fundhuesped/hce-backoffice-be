#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Problem
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
import reversion

@reversion.register()
class PatientProblem(models.Model):
    """
    Clase que representa un problema de un paciente
    """

    STATE_ACTIVE = 'Active'
    STATE_CLOSED = 'Closed'
    STATE_ERROR = 'Error'

    STATE_CHOICES = (
        (STATE_ACTIVE, 'Active'),
        (STATE_CLOSED, 'Closed'),
        (STATE_ERROR, 'Error')
    )

    observations = models.CharField(max_length=200, null=True)
    paciente = models.ForeignKey(Paciente, blank=True, null=False, on_delete=models.SET_NULL)
    problem = models.ForeignKey(Problem, null=False, on_delete=models.CASCADE)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)
    profesional = models.ForeignKey(User, null=False, on_delete=models.SET_NULL)
    createdOn = models.DateTimeField(auto_now=True)
    startDate = models.DateField(blank=True, null=True)
    closeDate = models.DateField(blank=True, null=True)
    aditionalData = JSONField(null=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state','-startDate', 'problem__name']
