#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_hce.models import PatientProblem
from django.contrib.auth.models import User
import reversion

@reversion.register()
class PatientARVPrescription(models.Model):
    """
    Clase que representa un problema de un paciente
    """

    TYPE_VACCINE = 'Vaccine'
    TYPE_ARV = 'Arv'
    TYPE_PROF = 'Prophylaxis'
    TYPE_GENERAL = 'General'

    TYPE_CHOICES = (
        (TYPE_VACCINE, 'Vaccine'),
        (TYPE_ARV, 'Arv'),
        (TYPE_PROF, 'Prophylaxis'),
        (TYPE_GENERAL, 'General')
    )


    paciente = models.ForeignKey(Paciente, blank=True, null=False)

    prescripctionType = models.CharField(max_length=20,
                                         choices=TYPE_CHOICES,
                                         default=TYPE_GENERAL)
    observations = models.CharField(max_length=200, null=True)
    createdOn = models.DateTimeField(auto_now=True)
    issuedDate = models.DateField(null=False)
    createdBy = models.ForeignKey(User, null=False)
    duplicateRequired = models.BooleanField(default=False)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['-createdOn']
