#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class OrderedType(models.Model):
    """
    Clase que representa un modelo ordenado
    """

    order = models.IntegerField(null=True)
    class Meta:
        """
        Metadata de la clase
        """
        abstract = True
        ordering = ['order']
