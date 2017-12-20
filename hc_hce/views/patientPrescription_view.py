#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientPrescriptionNestSerializer
from hc_hce.models import Visit
from hc_hce.models import PatientPrescription
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class PatientPrescriptionList(PaginateListCreateAPIView):
    serializer_class = PatientPrescriptionNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = PatientPrescription.objects.all()

        patient_id = self.kwargs.get('pacienteId')
        if patient_id is not None:
            queryset = queryset.filter(paciente=patient_id)

        startDate = self.request.query_params.get('startDate')
        if startDate is not None:
            queryset = queryset.filter(issuedDate_gte=startDate)

        endDate = self.request.query_params.get('endDate')
        if endDate is not None:
            queryset = queryset.filter(issuedDate_lte=endDate)

        prescripctionType = self.request.query_params.get('prescripctionType')
        if prescripctionType is not None:
            queryset = queryset.filter(prescripctionType=prescripctionType)

        return queryset


    def create(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')
        profesional = self.request.user

        data = request.data.copy()
        data['paciente'] = patient_id
        data['createdBy'] = profesional.id
        visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
        if visits.count()==0:
            paciente = Paciente.objects.filter(pk=patient_id).get()
            Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )

        serializer = PatientPrescriptionNestSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class PatientPrescriptionDetail(generics.RetrieveAPIView):
    serializer_class = PatientPrescriptionNestSerializer
    queryset = PatientPrescription.objects.all()
    # permission_classes = (DjangoModelPermissions,)