#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientVaccinePrescriptionNestSerializer
from hc_hce.models import Visit
from hc_hce.models import PatientVaccinePrescription
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta  
from datetime import datetime

class PatientVaccinePrescriptionList(PaginateListCreateAPIView):
    serializer_class = PatientVaccinePrescriptionNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = PatientVaccinePrescription.objects.all()

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
        # TODO Remove to new class

        visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
        if visits.count()==0:
            paciente = Paciente.objects.filter(pk=patient_id).get()
            Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )

        if data['cantRecetas'] and data['cantRecetas'] > 1:

            prescriptionsIds = []
            originalDate = data['issuedDate']
            for x in range(0,data['cantRecetas']):
                data['issuedDate'] = datetime.strptime(originalDate, "%Y-%m-%dT%H:%M:%S.000Z").date() + timedelta(days=28*(x+1))  
                serializer = PatientVaccineNestSerializer(data=data, context={'request': request})
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                prescriptionsIds.append(serializer.data['id'])
            return Response({"prescriptionsIds":prescriptionsIds})

        else:
            serializer = PatientVaccineNestSerializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return Response(serializer.data)

class PatientVaccinePrescriptionDetail(generics.RetrieveAPIView):
    serializer_class = PatientVaccinePrescriptionNestSerializer
    queryset = PatientVaccinePrescription.objects.all()
    # permission_classes = (DjangoModelPermissions,)
