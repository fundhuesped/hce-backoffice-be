#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Medication

class PatientMedication(models.Model):
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

    paciente = models.ForeignKey(Paciente,blank=True, null=False)
    medication = models.ForeignKey(Medication, null=False)


    observations = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)
    createdOn = models.DateTimeField(auto_now=True)
    startDate = models.DateField(blank=True, null=True)
    closeDate = models.DateField(blank=True, null=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state','-startDate', 'medication__name']
