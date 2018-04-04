#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_masters.models import MedicationType


class Vaccine(ActiveModel):
    """
    Clase que representa un medicamento
    """

    name = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    synonym = models.CharField(max_length=150, null=True)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['name']
