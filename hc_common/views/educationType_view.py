#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_common.serializers import EducationTypeNestSerializer
from hc_common.models import EducationType
from hc_core.views import PaginateListCreateAPIView


class EducationTypeList(PaginateListCreateAPIView):
    serializer_class = EducationTypeNestSerializer
    queryset = EducationType.objects.all()
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = EducationType.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class EducationTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationTypeNestSerializer
    queryset = EducationType.objects.all()
    permission_classes = (DjangoModelPermissions,)
