#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from django.contrib.auth.models import User
from hc_pacientes.models import Paciente
import reversion

@reversion.register()
class Visit(ActiveModel):
    """
    Clase que representa un problema
    """

    STATE_OPEN = 'Open'
    STATE_CLOSED = 'Closed'
    STATE_CANCELED = 'Canceled'

    STATE_CHOICES = (
        (STATE_OPEN, 'Open'),
        (STATE_CLOSED, 'Closed'),
        (STATE_CANCELED, 'Canceled')
    )


    profesional = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    paciente = models.ForeignKey(Paciente, null=False, on_delete=models.DO_NOTHING)
    notaClinica = models.CharField(max_length=2000, null=True)
    reason = models.CharField(max_length=200, null=True)
    visitType = models.CharField(max_length=30, null=True)
    created_on = models.DateTimeField(auto_now=True)
    closed_on = models.DateTimeField(null=True)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_OPEN)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['status', '-date']
