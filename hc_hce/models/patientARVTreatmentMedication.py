#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Medication
from hc_hce.models import PatientProblem
from hc_hce.models import PatientARVTreatment

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

    medication = models.ForeignKey(Medication, null=True, blank=True)
    patientARVTreatment = models.ForeignKey(PatientARVTreatment, null=True, blank=True, related_name='patientARVTreatmentMedications')
    quantityPerDay = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    quantityPerMonth = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state','medication']
