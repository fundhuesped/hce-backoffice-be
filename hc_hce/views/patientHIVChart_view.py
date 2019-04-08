#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_laboratory.serializers import LabResultNestSerializer
from hc_laboratory.serializers import DeterminacionValorNestSerializer
from hc_hce.models import PatientProblem
from hc_laboratory.models import DeterminacionValor
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class PatientHIVChart(generics.RetrieveAPIView):
    # permission_classes = (DjangoModelPermissions,)

    def get(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')
        patientProblem = PatientProblem.objects.filter(paciente=patient_id, problem=1880, state=PatientProblem.STATE_ACTIVE)
        if patientProblem.exists():
            return Response(patientProblem[0].aditionalData)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)