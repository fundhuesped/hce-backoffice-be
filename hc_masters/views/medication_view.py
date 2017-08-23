#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_masters.serializers import MedicationNestSerializer
from hc_masters.models import Medication
from hc_core.views import PaginateListCreateAPIView


class MedicationList(PaginateListCreateAPIView):
    serializer_class = MedicationNestSerializer
    queryset = Medication.objects.all()
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Medication.objects.all()
        name = self.request.query_params.get('name')
        composition = self.request.query_params.get('composition')
        status = self.request.query_params.get('status')
        medicationType = self.request.query_params.get('medicationType')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if composition is not None:
            queryset = queryset.filter(composition_icontains=composition)
        if medicationType is not None:
            queryset = queryset.filter(medicationType=medicationType)
        return queryset


class MedicationDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationNestSerializer
    queryset = Medication.objects.all()
    # permission_classes = (DjangoModelPermissions,)
