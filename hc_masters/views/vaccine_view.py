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
            queryset = queryset.filter(Q(name__unaccent__icontains=name) | Q(synonym__unaccent__icontains=name))
        if status is not None:
            queryset = queryset.filter(status=status)
        print queryset.all()[0].name
        print queryset.all()[1].name
        print queryset.all()[2].name
        print queryset.all()[3].name
        print queryset.all()[4].name
        print queryset.all()[5].name
        return queryset


class VaccineDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VaccineNestSerializer
    queryset = Vaccine.objects.all()
    # permission_classes = (DjangoModelPermissions,)
