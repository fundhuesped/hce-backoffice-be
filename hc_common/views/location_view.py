#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_common.serializers import LocationNestSerializer
from hc_common.models import Location
from hc_core.views import PaginateListCreateAPIView


class LocationList(PaginateListCreateAPIView):
    serializer_class = LocationNestSerializer
    queryset = Location.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Location.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        district = self.request.query_params.get('district')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if district is not None:
            queryset = queryset.filter(district_id=district)
        return queryset


class LocationDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationNestSerializer
    queryset = Location.objects.all()
    permission_classes = (DjangoModelPermissions,)
