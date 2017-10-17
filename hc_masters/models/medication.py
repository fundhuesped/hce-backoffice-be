#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_masters.models import MedicationType


class Medication(ActiveModel):
    """
    Clase que representa un medicamento
    """

    name = models.CharField(max_length=150, null=False)
    composition = models.CharField(max_length=150, null=True)
    abbreviation = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    medicationType = models.ForeignKey(MedicationType)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['name']