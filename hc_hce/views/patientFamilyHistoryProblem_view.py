#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import pytz

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientFamilyHistoryProblemNestSerializer
from hc_hce.models import PatientFamilyHistoryProblem
from hc_hce.models import Visit
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
        profesional = self.request.user

        data = request.data.copy()
        data['paciente'] = patient_id
        data['profesional'] = profesional.id
        visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE)
        paciente = Paciente.objects.filter(pk=patient_id).get()

        if visits.count()==0:
            visit = Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )

        serializer = PatientFamilyHistoryProblemNestSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
class PatientFamilyHistoryProblemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientFamilyHistoryProblemNestSerializer
    queryset = PatientFamilyHistoryProblem.objects.all()
    # permission_classes = (DjangoModelPermissions,)


    def update(self, request, *args, **kwargs):
        profesional = self.request.user
        instance = self.get_object()

        diff = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - instance.createdOn
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600


        if hours > 8:
            if instance.profesional.id != request.data['profesional']['id']:
                return Response('Solo se puede modificar por el usuario que lo creo', status=status.HTTP_400_BAD_REQUEST)

            elif instance.state == Visit.STATE_OPEN and request.data['state'] == Visit.STATE_CLOSED:
                instance.state = Visit.STATE_CLOSED
                instance.save()
                # Continues down

            else:
                if instance.state == Visit.STATE_OPEN:
                    instance.state = Visit.STATE_CLOSED
                    instance.save()
                    return Response('Visita cerrada automaticamente luego de 8 horas', status=status.HTTP_400_BAD_REQUEST)

        # visits = Visit.objects.filter(paciente=request.data['paciente']['id'], profesional=profesional.id, status=Visit.STATUS_ACTIVE)
        # paciente = Paciente.objects.filter(pk=request.data['paciente']['id']).get()

        # if visits.count()==0:
        #     visit = Visit.objects.create(
        #         profesional=profesional,
        #         paciente=paciente,
        #     )
        return super(PatientFamilyHistoryProblemDetail, self).update(request, *args, **kwargs)


