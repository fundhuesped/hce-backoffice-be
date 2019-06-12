#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_laboratory.models import CategoriaDeterminacion


class Determinacion(ActiveModel):
    """
    Clase que representa una determinacion de laboratorio
    """
    code = models.CharField(max_length=50, null=False)
    label = models.CharField(max_length=50, null=False)
    unitOfMeasure = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    order = models.IntegerField(null=True)
    category = models.ForeignKey(CategoriaDeterminacion, null=True, on_delete=models.SET_NULL)
    upperLimit = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    lowerLimit = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['order']
