#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_masters.serializers import ProblemNestSerializer
from hc_masters.models import Problem
from hc_core.views import PaginateListCreateAPIView


class ProblemList(PaginateListCreateAPIView):
    serializer_class = ProblemNestSerializer
    queryset = Problem.objects.all()
    filter_backends = (filters.OrderingFilter,)
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Problem.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        problemType = self.request.query_params.get('problemType')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        if problemType is not None:
            queryset = queryset.filter(problemType=problemType)
        return queryset


class ProblemDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProblemNestSerializer
    queryset = Problem.objects.all()
    # permission_classes = (DjangoModelPermissions,)
