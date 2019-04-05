#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_hce.models import PatientProblem
from django.contrib.auth.models import User

class ProblemHivDetails(models.Model):
    """
    Clase que representa los detalles de un problema de HIV
    """

    problem = models.ForeignKey(PatientProblem, blank=False, null=False)
    
    # TODO translate fields and make required changes in the frontend, I cannot do it now because deadlines
    # TODO include string choices as a type

    vertical = models.BooleanField(default=False)
    mujeres = models.BooleanField(default=False)
    hombres = models.BooleanField(default=False)
    trans = models.BooleanField(default=False)
    inyeccion = models.BooleanField(default=False)
    accidente = models.BooleanField(default=False)
    transfusion = models.BooleanField(default=False)
    institucion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    otra = models.BooleanField(default=False)
    cual = models.CharField(max_length=200, null=True)
    desconocida = models.BooleanField(default=False)
    clinicalState = models.CharField(max_length=200, null=False)
    woman = models.CharField(max_length=200, null=True)

    createdOn = models.DateTimeField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['-createdOn']
