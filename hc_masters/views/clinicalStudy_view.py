#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_masters.serializers import ClinicalStudyNestSerializer
from hc_masters.models import ClinicalStudy
from hc_core.views import PaginateListCreateAPIView
from django.db.models import Q

class ClinicalStudyList(PaginateListCreateAPIView):
    serializer_class = ClinicalStudyNestSerializer
    queryset = ClinicalStudy.objects.all()
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = ClinicalStudy.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(Q(name__icontains=name) | Q(synonym__icontains=name))
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class ClinicalStudyDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClinicalStudyNestSerializer
    queryset = ClinicalStudy.objects.all()
    # permission_classes = (DjangoModelPermissions,)
