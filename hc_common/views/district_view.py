#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_common.serializers import DistrictNestSerializer
from hc_common.models import District
from hc_core.views import PaginateListCreateAPIView

class DistrictList(PaginateListCreateAPIView):
    serializer_class = DistrictNestSerializer
    queryset = District.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = District.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        province = self.request.query_params.get('province')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if province is not None:
            queryset = queryset.filter(province_id=province)
        return queryset


class DistrictDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DistrictNestSerializer
    queryset = District.objects.all()
    permission_classes = (DjangoModelPermissions,)
