#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_common.serializers import ProvinceNestSerializer
from hc_common.models import Province
from hc_core.views import PaginateListCreateAPIView


class ProvinceList(PaginateListCreateAPIView):
    serializer_class = ProvinceNestSerializer
    queryset = Province.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Province.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class ProvinceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProvinceNestSerializer
    queryset = Province.objects.all()
    permission_classes = (DjangoModelPermissions,)
