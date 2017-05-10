#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from hc_pacientes.serializers import PacienteNestSerializer
from hc_pacientes.models import Paciente
from hc_core.views import PaginateListCreateAPIView

from rest_framework import serializers


class PacienteList(PaginateListCreateAPIView):
    """
    Vista para listar Pacientes existentes, o crear un nuevo Paciente
    """
    serializer_class = PacienteNestSerializer
    queryset = Paciente.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Paciente.objects.all()


        firstName = self.request.query_params.get('firstName')
        fatherSurname = self.request.query_params.get('fatherSurname')
        status = self.request.query_params.get('status')
        documentType = self.request.query_params.get('documentType')
        document = self.request.query_params.get('documentNumber')
        birthDate = self.request.query_params.get('birthDate')

        if firstName is None and fatherSurname is None and documentType is None and document is None and birthDate is None:
            raise serializers.ValidationError({'error': 'Se debe realizar una consulta con parametros de busqueda validos'})

        if firstName is not None :
            if  len(firstName) >= 3:
                queryset = queryset.filter(firstName__istartswith=firstName)
            else:
                raise serializers.ValidationError({'error': 'Se debe realizar una consulta con parametros de busqueda validos'})

        if fatherSurname is not None:
            if len(fatherSurname) >= 3:
                queryset = queryset.filter(fatherSurname__istartswith=fatherSurname)
            else:
                raise serializers.ValidationError({'error': 'Se debe realizar una consulta con parametros de busqueda validos'})

        if status is not None:
            queryset = queryset.filter(status=status)
            
        if documentType is not None:
            if document is not None:
                queryset = queryset.filter(documentType=documentType)
            else:
                raise serializers.ValidationError({'error': 'Se debe realizar una consulta con parametros de busqueda validos'})
        if document is not None:
            if documentType is not None:
                queryset = queryset.filter(documentNumber=document)
            else:
                raise serializers.ValidationError({'error': 'Se debe realizar una consulta con parametros de busqueda validos'})
        if birthDate is not None:
            queryset = queryset.filter(birthDate=birthDate)


        #Order  
        order_field = self.request.query_params.get('order_field')
        order_by = self.request.query_params.get('order_by')
        if (order_field is not None) and (order_by is not None):
            if order_by == 'asc':
                queryset = queryset.order_by(order_field)
            else:
                if order_by == 'desc':
                    queryset = queryset.order_by('-'+order_field)
        return queryset


class PacienteDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un paciente
    """
    serializer_class = PacienteNestSerializer
    queryset = Paciente.objects.all()
    # permission_classes = (IsAuthenticated,)
