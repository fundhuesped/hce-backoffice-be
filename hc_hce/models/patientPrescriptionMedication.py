#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Medication
from hc_hce.models import PatientPrescription
from django.contrib.auth.models import User

class PatientPrescriptionMedication(models.Model):
    """
    Clase que representa un medicamento prescripto en una receta
    """

    medication = models.ForeignKey(Medication, null=False)
    quantityPerDay = models.IntegerField(null=True)
    dayCount = models.IntegerField(null=True)
    prescription = models.ForeignKey(PatientPrescription, null=False, related_name='prescriptedMedications')
    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['medication']
