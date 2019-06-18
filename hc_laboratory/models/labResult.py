#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from django.contrib.auth.models import User
import reversion

@reversion.register()
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

    INPUTTYPE_AUTOMATIC = 'Automatic'
    INPUTTYPE_MANUAL = 'Manual'

    INPUTTYPE_CHOICES = (
        (INPUTTYPE_AUTOMATIC, 'Manual'),
        (INPUTTYPE_MANUAL, 'Automatico')
    )

    paciente = models.ForeignKey(Paciente, null=False, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=8,
                              choices=STATUS_CHOICES,
                              default=STATUS_ACTIVE)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    createdOn = models.DateTimeField(auto_now=True)
    modifiedOn = models.DateTimeField(auto_now=False, null=True)
    inputType = models.CharField(max_length=10,
                                 choices=INPUTTYPE_CHOICES,
                                 default=INPUTTYPE_MANUAL)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['status','-date']
