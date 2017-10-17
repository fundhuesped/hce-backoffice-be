#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Medication
from hc_hce.models import PatientProblem

class PatientARVTreatment(models.Model):
    """
    Clase que representa un tratamiento ARV de un paciente
    """

    STATE_ACTIVE = 'Active'
    STATE_CLOSED = 'Closed'
    STATE_ERROR = 'Error'

    STATE_CHOICES = (
        (STATE_ACTIVE, 'Active'),
        (STATE_CLOSED, 'Closed'),
        (STATE_ERROR, 'Error')
    )
    CHANGE_TOXICITY = 'Toxicidad'
    CHANGE_ABANDON = 'Abandono'
    CHANGE_FAILURE = 'Fallo'
    CHANGE_SIMPLIFICATION = 'Simplificacion'

    CHANGE_CHOICES = (
        (CHANGE_TOXICITY, 'Toxicidad'),
        (CHANGE_ABANDON, 'Abandono'),
        (CHANGE_SIMPLIFICATION, 'Simplificacion'),
        (CHANGE_FAILURE, 'Fallo')
    )

    paciente = models.ForeignKey(Paciente,blank=True, null=False)
    medications = models.ManyToManyField(Medication)
    patientProblem = models.ForeignKey(PatientProblem, null=True, blank=True)

    observations = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)
    changeReason = models.CharField(max_length=20,
                             choices=CHANGE_CHOICES, null=True)
    createdOn = models.DateTimeField(auto_now=True)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state','-startDate']
