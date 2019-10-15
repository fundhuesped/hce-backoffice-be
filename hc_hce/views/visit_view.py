#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import pytz
from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import VisitNestSerializer
from hc_hce.models import Visit
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from hc_hce.services.visitService import schedule_close

class PacienteVisitList(PaginateListCreateAPIView):
    serializer_class = VisitNestSerializer
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Visit.objects.all()
        pacienteId = self.kwargs.get('pacienteId')
        queryset = queryset.filter(paciente=pacienteId)

        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        state = self.request.query_params.get('state')
        if state is not None:
            queryset = queryset.filter(state=state)

        not_state = self.request.query_params.get('notState')
        if not_state is not None:
            queryset = queryset.exclude(state__in=not_state.split(','))

        not_status = self.request.query_params.get('notStatus')
        if not_status is not None:
            queryset = queryset.exclude(status__in=not_status.split(','))

        fromDate = self.request.query_params.get('fromDate')
        if fromDate is not None:
            queryset = queryset.filter(date__gte=fromDate)

        toDate = self.request.query_params.get('toDate')
        if toDate is not None:
            queryset = queryset.filter(date__lte=toDate)

        return queryset

    def create(self, request, *args, **kwargs):
        profesional = request.user
        data = request.data.copy()
        data['profesional'] = profesional.id
        data['paciente'] = self.kwargs.get('pacienteId')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if serializer.data['id'] is not None:
            schedule_close(serializer.data['id'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class VisitDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VisitNestSerializer
    queryset = Visit.objects.all()
    # permission_classes = (DjangoModelPermissions,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        diff = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - instance.created_on
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600


        if hours > 8:
            if instance.profesional.id != request.data['profesional']['id']:
                return Response('Solo se puede modificar por el usuario que lo creo', status=status.HTTP_400_BAD_REQUEST)

            elif instance.state == Visit.STATE_OPEN and request.data['state'] == Visit.STATE_CLOSED:
                instance.state = Visit.STATE_CLOSED
                instance.save();
                serializer = self.get_serializer(instance)
                return Response(serializer.data)

            else:
                if instance.state == Visit.STATE_OPEN:
                    instance.state = Visit.STATE_CLOSED
                    instance.save();
                    return Response('Visita cerrada automaticamente luego de 8 horas', status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class CurrentVisitDetail(generics.RetrieveUpdateAPIView):
    serializer_class = VisitNestSerializer
    queryset = Visit.objects.all()

    def retrieve(self, request, *args, **kwargs):
        queryset = Visit.objects.all()
        pacienteId = self.kwargs.get('pacienteId')
        profesional = self.request.user
        queryset = queryset.filter(paciente=pacienteId)
        queryset = queryset.filter(profesional=profesional.id)
        queryset = queryset.filter(status=Visit.STATUS_ACTIVE)
        date_max_allowed = datetime.datetime.utcnow().replace(tzinfo=pytz.utc).replace(hour=18, minute=00)
        date_min_allowed = datetime.datetime.utcnow().replace(tzinfo=pytz.utc).replace(hour=00, minute=00)
        queryset = queryset.filter(created_on__gt=date_min_allowed)
        queryset = queryset.filter(created_on__lte=date_max_allowed)
        try:
            serializer = self.get_serializer(queryset.get())
            return Response(serializer.data)
        except (TypeError, ValueError, ObjectDoesNotExist):
            raise Http404
