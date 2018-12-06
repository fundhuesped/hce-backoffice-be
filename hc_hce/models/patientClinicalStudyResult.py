#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import ClinicalStudy
from django.contrib.auth.models import User

class PatientClinicalStudyResult(models.Model):
    """
    Clase que representa un problema de un paciente
    """

    STATE_ACTIVE = 'Active'
    STATE_ERROR = 'Error'

    STATE_CHOICES = (
        (STATE_ACTIVE, 'Active'),
        (STATE_ERROR, 'Error')
    )

    observations = models.CharField(max_length=2000, null=True)
    clinicalStudy = models.ForeignKey(ClinicalStudy,blank=True, null=False)
    paciente = models.ForeignKey(Paciente,blank=True, null=False)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)
    createdOn = models.DateTimeField(auto_now=True)
    studyDate = models.DateField(blank=True, null=True)
    profesional = models.ForeignKey(User, null=False)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state', '-studyDate', 'clinicalStudy__name', ]
