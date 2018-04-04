#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import AbstractType


class OrderedAbstractType(AbstractType):
    """
    Clase que representa un modelo abstracto genérico, base para todos los demas modelos
    """

    order = models.IntegerField(null=True)
    class Meta:
        """
        Metadata de la clase
        """
        abstract = True
        ordering = ['order']
