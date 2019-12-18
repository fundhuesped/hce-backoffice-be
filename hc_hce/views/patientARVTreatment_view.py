#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
import pytz

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

        not_state = self.request.query_params.get('notState')
        if not_state is not None:
            queryset = queryset.exclude(state=not_state)

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
        problem_startDate = self.request.data['startDate']
        birth_date = Paciente.objects.filter(pk=patient_id).get().birthDate  
        problem_endDate = self.request.data['endDate']

        data = request.data.copy()
        data['paciente'] = patient_id
        data['profesional'] = profesional.id

        comparable_problem_startDate = datetime.strptime(problem_startDate, "%Y-%m-%d").date()
        assert birth_date <= comparable_problem_startDate,"La fecha ingresada es anterior a la fecha de nacimiento"

        if data['state'] == 'Closed' :

            comparable_problem_endDate = datetime.strptime(problem_endDate, "%Y-%m-%d").date()
            assert comparable_problem_startDate < comparable_problem_endDate,"La fecha de finalización no puede ser anterio a la fecha de inicio"

            visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE)
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

                visits = Visit.objects.filter(paciente=patient_id, profesional=profesional.id, status=Visit.STATUS_ACTIVE)
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
        instance = self.get_object()
        problem_startDate = self.request.data['startDate']
        problem_endDate = self.request.data['endDate']

        comparable_problem_startDate = datetime.strptime(problem_startDate, "%Y-%m-%d").date()
        comparable_problem_endDate = datetime.strptime(problem_endDate, "%Y-%m-%d").date()
        assert comparable_problem_startDate < comparable_problem_endDate,"La fecha de finalización no puede ser anterior a la fecha de inicio"

        diff = datetime.utcnow().replace(tzinfo=pytz.utc) - instance.createdOn
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

        visits = Visit.objects.filter(paciente=request.data['paciente']['id'], profesional=profesional.id, status=Visit.STATUS_ACTIVE)
        paciente = Paciente.objects.filter(pk=request.data['paciente']['id']).get()

        if visits.count()==0:
            visit = Visit.objects.create(
                profesional=profesional,
                paciente=paciente,
            )
        return super(PatientARVTreatmentDetail, self).update(request, *args, **kwargs)
