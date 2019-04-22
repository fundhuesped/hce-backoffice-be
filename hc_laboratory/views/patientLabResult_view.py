#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import pytz

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_laboratory.serializers import LabResultNestSerializer
from hc_laboratory.serializers import DeterminacionValorNestSerializer
from hc_hce.models import Visit
from hc_laboratory.models import LabResult
from hc_laboratory.models import DeterminacionValor
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from hc_core.exceptions import FailedDependencyException
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

class PatientLabResults(PaginateListCreateAPIView):
    serializer_class = LabResultNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        patient_id = self.kwargs.get('pacienteId')

        queryset = LabResult.objects.filter(paciente=patient_id)

        state = self.request.query_params.get('state')
        if state is not None:
            queryset = queryset.filter(state=state)

        not_state = self.request.query_params.get('notState')
        if not_state is not None:
            queryset = queryset.exclude(state=not_state)

        startDate = self.request.query_params.get('startDate')
        if startDate is not None:
            queryset = queryset.filter(date_gte=startDate)

        endDate = self.request.query_params.get('endDate')
        if endDate is not None:
            queryset = queryset.filter(date_lte=endDate)

        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(date=date)

        return queryset


    def create(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')
        profesional = self.request.user

        data = request.data.copy()
        data['paciente'] = patient_id

        visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
        if visits.count()==0:
            paciente = Paciente.objects.filter(pk=patient_id).get()
            visit = Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )

        results = LabResult.objects.filter(paciente=patient_id, date=data['date'])
        if results.count()==1:
            labResult = self.updateResults(results[0],data)
            return Response(status=status.HTTP_200_OK)
        else:

            serializer = LabResultNestSerializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)

    def updateResults(self, result, data):
        for value in data['values']:
            found = False
            for saved_value in result.values.all():
                if saved_value.determinacion.id == value['determinacion']['id']:
                    found = True
                    saved_value.value = value['value']
                    saved_value.save()
                    break
            if not found:
                value['labResult'] = result.id
                serializer = DeterminacionValorNestSerializer(data=value)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return result



class PatientCD4Detail(generics.RetrieveAPIView):
    serializer_class = LabResultNestSerializer
    queryset = LabResult.objects.all()
    # permission_classes = (DjangoModelPermissions,)

    def get(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')
        determinacion = DeterminacionValor.objects.filter(labResult__paciente=patient_id, determinacion__code="CD4", labResult__status=LabResult.STATUS_ACTIVE).order_by('-labResult__createdOn')
        if determinacion.exists():
            return Response({ "date": determinacion[0].labResult.date,"value": determinacion[0].value, "unitOfMeasure": determinacion[0].determinacion.unitOfMeasure})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PatientCVDetail(generics.RetrieveAPIView):
    serializer_class = LabResultNestSerializer
    queryset = LabResult.objects.all()
    # permission_classes = (DjangoModelPermissions,)

    def get(self, request, *args, **kwargs):
        patient_id = self.kwargs.get('pacienteId')
        determinacion = DeterminacionValor.objects.filter(labResult__paciente=patient_id, determinacion__code="CARGA VIRAL", labResult__status=LabResult.STATUS_ACTIVE).order_by('-labResult__createdOn')
        if determinacion.exists():
            return Response({ "date": determinacion[0].labResult.date,"value": determinacion[0].value, "unitOfMeasure": determinacion[0].determinacion.unitOfMeasure})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PatientLabResultDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LabResultNestSerializer
    queryset = LabResult.objects.all()
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

                else:
                    return Response('Solo se pueden modificar dentro de las 8 horas', status=status.HTTP_400_BAD_REQUEST)

        visits = Visit.objects.filter(paciente=request.data['paciente']['id'], profesional=profesional.id, status=Visit.STATUS_ACTIVE, state=Visit.STATE_OPEN)
        paciente = Paciente.objects.filter(pk=request.data['paciente']['id']).get()

        if visits.count()==0:
            visit = Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )
        return super(PatientLabResultDetail, self).update(request, *args, **kwargs)
