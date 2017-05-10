#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from django.contrib.auth.models import User
from hc_pacientes.models import Paciente


class Visit(ActiveModel):
    """
    Clase que representa un problema
    """

    STATE_OPEN = 'Open'
    STATE_CLOSED = 'Closed'

    STATE_CHOICES = (
        (STATE_OPEN, 'Open'),
        (STATE_CLOSED, 'Closed')
    )


    profesional = models.ForeignKey(User)
    paciente = models.ForeignKey(Paciente)
    notaClinica = models.CharField(max_length=1000)

    created_on = models.DateField(auto_now=True)
    date = models.DateField(auto_now=True)

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
        ordering = ['-date']
