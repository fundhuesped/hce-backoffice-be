#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import AbstractType


class SocialService(AbstractType):
    """
    Clase que representa la obra social de una persona
    """
    order = models.IntegerField(default=0, null=True)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['-order','name']
