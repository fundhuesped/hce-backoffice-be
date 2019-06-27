#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_common.models import ActiveModel
from hc_hce.models import Visit

class VisitEvent(models.Model):
    """
    Clase que representa un evento 
    """

    TYPE_NEW_PROBLEM = 'NewProblem'
    TYPE_CLOSE_PROBLEM = 'CloseProlem'
    TYPE_MODIFY_PROBLEM = 'ModifyProblem'

    TYPE_NEW_FAMILY_PROBLEM = 'NewFamliyProblem'
    TYPE_CLOSE_FAMILY_PROBLEM = 'CloseFamilyProblem'
    TYPE_MODIFY_FAMILY_PROBLEM = 'ModifyFamilyProblem'

    STATE_CHOICES = (
        (TYPE_NEW_PROBLEM, 'NewProblem'),
        (TYPE_CLOSE_PROBLEM, 'CloseProlem'),
        (TYPE_MODIFY_PROBLEM, 'ModifyProblem'),
        (TYPE_NEW_FAMILY_PROBLEM, 'NewFamliyProblem'),
        (TYPE_CLOSE_FAMILY_PROBLEM, 'CloseFamilyProblem'),
        (TYPE_MODIFY_FAMILY_PROBLEM, 'ModifyFamilyProblem')
    )

    visit = models.ForeignKey(Visit, related_name='events', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=8,
                              choices=ActiveModel.STATUS_CHOICES,
                              default=ActiveModel.STATUS_ACTIVE)
    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']
