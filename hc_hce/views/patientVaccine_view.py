#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientVaccineNestSerializer
from hc_hce.models import PatientVaccine
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class PatientVaccineList(PaginateListCreateAPIView):
    serializer_class = PatientVaccineNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        patient_id = self.kwargs.get('pacienteId')

        queryset = PatientVaccine.objects.filter(paciente=patient_id)

        state = self.request.query_params.get('state')
        if state is not None:
            queryset = queryset.filter(state=state)

        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(vaccine_name=name)

        appliedDate = self.request.query_params.get('appliedDate')
        if appliedDate is not None:
            queryset = queryset.filter(appliedDate=appliedDate)

        return queryset


    def create(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')

        data = request.data.copy()
        data['paciente'] = patient_id
        serializer = PatientVaccineNestSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
        
class PatientVaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientVaccineNestSerializer
    queryset = PatientVaccine.objects.all()
    # permission_classes = (DjangoModelPermissions,)
