#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_masters.serializers import VaccineNestSerializer
from hc_masters.models import Vaccine
from hc_core.views import PaginateListCreateAPIView
from django.db.models import Q

class VaccineList(PaginateListCreateAPIView):
    serializer_class = VaccineNestSerializer
    queryset = Vaccine.objects.all()
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Vaccine.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(Q(name__icontains=name) | Q(synonym__icontains=name))
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class VaccineDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VaccineNestSerializer
    queryset = Vaccine.objects.all()
    # permission_classes = (DjangoModelPermissions,)
