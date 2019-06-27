#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_masters.models import Medication


class MedicationPresentation(ActiveModel):
    """
    Clase que representa un medicamento
    """

    name = models.CharField(max_length=150, null=False)
    administrationType = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    medication = models.ForeignKey(Medication, related_name='presentations', on_delete=models.DO_NOTHING)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['name']