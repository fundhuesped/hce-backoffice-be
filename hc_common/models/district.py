#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import AbstractType, Province


class District(AbstractType):
    """
    Clase que representa un distrito donde vive una persona
    """
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
