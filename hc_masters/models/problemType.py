#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel


class ProblemType(ActiveModel):
    """
    Clase que representa al tipo de problema
    """

    name = models.CharField(max_length=150, null=False)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['name']