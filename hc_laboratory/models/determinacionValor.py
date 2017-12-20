#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_laboratory.models import LabResult
from hc_laboratory.models import Determinacion

class DeterminacionValor(ActiveModel):
    """
    Clase que representa un valor de una determinacion de laboratorio
    """
    labResult = models.ForeignKey(LabResult, blank=True, null=False, related_name='values')
    determinacion = models.ForeignKey(Determinacion, blank=True, null=False)
    value = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['labResult','determinacion']
