#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import CivilStatusTypeNestSerializer
from hc_common.models import CivilStatusType
from hc_core.views import PaginateListCreateAPIView
from rest_framework.permissions import DjangoModelPermissions

class CivilStatusTypeList(PaginateListCreateAPIView):
    serializer_class = CivilStatusTypeNestSerializer
    queryset = CivilStatusType.objects.all()
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = CivilStatusType.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')

        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)

        return queryset


class CivilStatusTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CivilStatusTypeNestSerializer
    queryset = CivilStatusType.objects.all()
    permission_classes = (DjangoModelPermissions,)
