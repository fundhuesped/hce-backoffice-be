#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Medication
from hc_hce.models import PatientARVPrescription
from django.contrib.auth.models import User

class PatientARVPrescriptionMedication(models.Model):
    """
    Clase que representa un medicamento prescripto en una receta
    """

    medication = models.ForeignKey(Medication, null=True, blank=True)
    quantityPerDay = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    quantityPerMonth = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    prescription = models.ForeignKey(PatientARVPrescription, null=True, related_name='prescriptedMedications')
    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['medication']
