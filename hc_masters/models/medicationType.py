#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel


class MedicationType(ActiveModel):
    """
    Clase que representa al tipo de medicamento
    """

    name = models.CharField(max_length=150, null=False)
    code = models.CharField(max_length=10, null=False)
    group = models.CharField(max_length=10, null=False)
    
    def __unicode__(self):
        return self.name + '(' + self.group + ')'

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['name']