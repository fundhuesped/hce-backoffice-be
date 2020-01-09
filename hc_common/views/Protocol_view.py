#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from hc_common.serializers import ProtocolNestSerializer
from hc_common.models import protocol
from hc_core.views import PaginateListCreateAPIView


class ProtocolList(PaginateListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Protocolo
    """
    serializer_class = ProtocolNestSerializer
    queryset = protocol.objects.all()

    def get_queryset(self):
        queryset = protocol.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class ProtocolDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Protocolo
    """
    serializer_class = ProtocolNestSerializer
    queryset = protocol.objects.all()
    #permission_classes = (AllowAny,)
