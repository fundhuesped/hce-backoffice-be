#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class ActiveModel(models.Model):
    """
    Clase base que implementa el concepto de entidad activa/inactiva
    """
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Activo'),
        (STATUS_INACTIVE, 'Inactivo')
    )

    class Meta:
        """
        Metadata de la clase
        """
        abstract = True
