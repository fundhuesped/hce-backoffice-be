#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_hce.models import PatientMedication
from hc_hce.models import PatientPrescription
from django.contrib.auth.models import User

class PatientPrescriptionMedication(models.Model):
    """
    Clase que representa un medicamento prescripto en una receta
    """

    patientMedication = models.ForeignKey(PatientMedication, null=True, blank=True, on_delete=models.SET_NULL)
    quantityPerDay = models.IntegerField(null=True)
    quantityPerMonth = models.IntegerField(null=True)
    prescription = models.ForeignKey(PatientPrescription, null=True, related_name='prescriptedMedications', on_delete=models.SET_NULL)
    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['patientMedication']
