#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from hc_pacientes.models import Paciente
from hc_masters.models import Problem
from django.contrib.auth.models import User
import reversion

@reversion.register()
class PatientFamilyHistoryProblem(models.Model):
    """
    Clase que representa un antecedente familiar
    """

    STATE_ACTIVE = 'Active'
    STATE_ERROR = 'Error'

    STATE_CHOICES = (
        (STATE_ACTIVE, 'Active'),
        (STATE_ERROR, 'Error')
    )

    RELATIONSHIP_MOTHER = 'Mother'
    RELATIONSHIP_FATHER = 'Father'
    RELATIONSHIP_OTHER = 'Other'
    RELATIONSHIP_BROTHER = 'Brother'
    RELATIONSHIP_GRANDMOTHER = 'Grandmother'
    RELATIONSHIP_GRANDFATHER = 'Grandfather'

    RELATIONSHIP_CHOICES = (
        (RELATIONSHIP_MOTHER, 'Mother'),
        (RELATIONSHIP_FATHER, 'Father'),
        (RELATIONSHIP_BROTHER, 'Brother'),
        (RELATIONSHIP_GRANDMOTHER, 'Grandmother'),
        (RELATIONSHIP_GRANDFATHER, 'Grandfather'),
        (RELATIONSHIP_OTHER, 'Other')
    )

    paciente = models.ForeignKey(Paciente,blank=True, null=False, on_delete=models.SET_NULL)
    problem = models.ForeignKey(Problem, null=False, on_delete=models.SET_NULL)
    profesional = models.ForeignKey(User, null=False, on_delete=models.SET_NULL)

    relationship = models.CharField(max_length=15,
                                    choices=RELATIONSHIP_CHOICES,
                                    default=RELATIONSHIP_OTHER)


    observations = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=8,
                             choices=STATE_CHOICES,
                             default=STATE_ACTIVE)
    createdOn = models.DateTimeField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['state', 'problem__name']
