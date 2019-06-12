#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_masters.models import ProblemType

class Problem(ActiveModel):
    """
    Clase que representa un problema
    """

    STATE_TO_REVIEW = 'ToReview'
    STATE_VALID = 'Valid'
    STATE_INVALID = 'Invalid'

    STATE_CHOICES = (
        (STATE_TO_REVIEW, 'ToReview'),
        (STATE_VALID, 'Valid'),
        (STATE_INVALID, 'Invalid')
    )



    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_TO_REVIEW)
    problemType = models.CharField(max_length=20, blank=True, null=True)
    problemTypeTmp = models.ForeignKey(ProblemType, null=True, on_delete=models.SET_NULL)

    class Meta:
        """
        Metadata de la clase
        """
        ordering = ['name']