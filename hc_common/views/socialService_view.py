#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_common.serializers import SocialServiceNestSerializer
from hc_common.models import SocialService
from hc_core.views import PaginateListCreateAPIView

class SocialServiceList(PaginateListCreateAPIView):
    serializer_class = SocialServiceNestSerializer
    queryset = SocialService.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = SocialService.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class SocialServiceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialServiceNestSerializer
    queryset = SocialService.objects.all()
    permission_classes = (DjangoModelPermissions,)
