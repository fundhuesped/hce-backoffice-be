#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientFamilyHistoryProblemNestSerializer
from hc_hce.models import PatientFamilyHistoryProblem
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class PatientFamilyHistoryProblemsList(PaginateListCreateAPIView):
    serializer_class = PatientFamilyHistoryProblemNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        patient_id = self.kwargs.get('pacienteId')
        queryset = PatientFamilyHistoryProblem.objects.filter(paciente=patient_id)

        state = self.request.query_params.get('state')
        if state is not None:
            queryset = queryset.filter(state=state)

        return queryset


    def create(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')

        data = request.data.copy()
        data['paciente'] = patient_id
        try:
            PatientFamilyHistoryProblem.objects.get(paciente=patient_id,problem=data['problem']['id'], state=PatientFamilyHistoryProblem.STATE_ACTIVE)
            raise FailedDependencyException('El problema a dar de alta ya esta activo')
        except (TypeError, ValueError, ObjectDoesNotExist):
            serializer = PatientFamilyHistoryProblemNestSerializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)
class PatientFamilyHistoryProblemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientFamilyHistoryProblemNestSerializer
    queryset = PatientFamilyHistoryProblem.objects.all()
    # permission_classes = (DjangoModelPermissions,)
