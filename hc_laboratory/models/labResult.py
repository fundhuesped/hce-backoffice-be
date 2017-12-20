#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente


class LabResult(models.Model):
    """
    Clase que representa un resultado de laboratorio
    """

    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_ERROR = 'Error'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo'),
        (STATUS_ERROR, 'Error')
    )
    paciente = models.ForeignKey(Paciente, null=False)
    date = models.DateField(auto_now=False)
    status = models.CharField(max_length=8,
                              choices=STATUS_CHOICES,
                              default=STATUS_ACTIVE)
    createdOn = models.DateTimeField(auto_now=True)
    modifiedOn = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['status','-date']
