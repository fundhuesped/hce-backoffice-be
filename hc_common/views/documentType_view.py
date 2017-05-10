#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from hc_common.serializers import DocumentTypeNestSerializer
from hc_common.models import DocumentType
from hc_core.views import PaginateListCreateAPIView

class DocumentTypeList(PaginateListCreateAPIView):
    """
    Vista para listar Documentos existentes, o crear un nuevo Documento
    """
    serializer_class = DocumentTypeNestSerializer
    queryset = DocumentType.objects.all()
    # permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = DocumentType.objects.all()
        name = self.request.query_params.get('name')
        status = self.request.query_params.get('status')
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset


class DocumentTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Documento
    """
    serializer_class = DocumentTypeNestSerializer
    queryset = DocumentType.objects.all()
    # permission_classes = (DjangoModelPermissions,)
