#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Medication
from hc_hce.models import PatientProblem
from hc_hce.models import PatientARVTreatment
from django.contrib.auth.models import User

class PatientARVTreatmentMedication(models.Model):
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

    medication = models.ForeignKey(Medication, null=True, blank=True, on_delete=models.SET_NULL)
    patientARVTreatment = models.ForeignKey(PatientARVTreatment, null=True, blank=True, related_name='patientARVTreatmentMedications', on_delete=models.SET_NULL)
    quantityPerDay = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    quantityPerMonth = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    profesional = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state','medication']
