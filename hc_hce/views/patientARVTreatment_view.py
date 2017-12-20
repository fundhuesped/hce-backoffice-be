#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientARVTreatmentNestSerializer
from hc_hce.models import Visit
from hc_hce.models import PatientARVTreatment
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class PatientARVTreartmentsList(PaginateListCreateAPIView):
    serializer_class = PatientARVTreatmentNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        patient_id = self.kwargs.get('pacienteId')

        queryset = PatientARVTreatment.objects.filter(paciente=patient_id)

        state = self.request.query_params.get('state')
        if state is not None:
            queryset = queryset.filter(state=state)

        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(Medication_name=name)

        startDate = self.request.query_params.get('startDate')
        if startDate is not None:
            queryset = queryset.filter(startDate=startDate)

        endDate = self.request.query_params.get('endDate')
        if endDate is not None:
            queryset = queryset.filter(endDate=endDate)

        return queryset


    def create(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')
        profesional = self.request.user

        data = request.data.copy()
        data['paciente'] = patient_id

        if data['state'] == 'Closed' :
            visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
            if visits.count()==0:
                paciente = Paciente.objects.filter(pk=patient_id).get()
                Visit.objects.create(
                    profesional=profesional,
                    paciente=paciente,
                )

        else :
            try:
                PatientARVTreatment.objects.get(paciente=patient_id, state=PatientARVTreatment.STATE_ACTIVE)
                raise FailedDependencyException('Ya existe un tratamiento activo')
            except (TypeError, ValueError, ObjectDoesNotExist):
                visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
                if visits.count()==0:
                    paciente = Paciente.objects.filter(pk=patient_id).get()
                    Visit.objects.create(
                        profesional=profesional,
                        paciente=paciente,
                    )

        serializer = PatientARVTreatmentNestSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

class PatientARVTreatmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientARVTreatmentNestSerializer
    queryset = PatientARVTreatment.objects.all()
    # permission_classes = (DjangoModelPermissions,)

    def update(self, request, *args, **kwargs):
        profesional = self.request.user
        print request.data['paciente']
        visits = Visit.objects.filter(paciente=request.data['paciente']['id'], profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
        paciente = Paciente.objects.filter(pk=request.data['paciente']['id']).get()

        if visits.count()==0:
            visit = Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )
        return super(PatientARVTreatmentDetail, self).update(request, *args, **kwargs)