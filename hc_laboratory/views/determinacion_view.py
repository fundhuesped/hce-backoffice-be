#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_laboratory.serializers import DeterminacionNestSerializer
from hc_laboratory.models import Determinacion
from hc_core.views import PaginateListCreateAPIView


class DeterminacionList(PaginateListCreateAPIView):
    serializer_class = DeterminacionNestSerializer
    queryset = Determinacion.objects.all()
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Determinacion.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__unaccent__icontains=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset

class DeterminacionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeterminacionNestSerializer
    queryset = Determinacion.objects.all()
    # permission_classes = (DjangoModelPermissions,)
