#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_practicas.serializers import ProfesionalNestSerializer
from hc_practicas.models import Profesional
from hc_core.views import PaginateListCreateAPIView

class ProfesionalList(PaginateListCreateAPIView):
    """
    Vista para listar Profesionales existentes, o crear un nuevo Paciente
    """
    serializer_class = ProfesionalNestSerializer
    queryset = Profesional.objects.all()
    filter_backends = (filters.OrderingFilter,)
    permission_classes = (DjangoModelPermissions,)


    def get_queryset(self):
        """
        Filtrado del queryset por nombre y primer apellido, si como mínimo tienen 3 caracteres, o el ID de prestación
        :return:
        """
        queryset = Profesional.objects.all()
        firstName = self.request.query_params.get('firstName')
        fatherSurename = self.request.query_params.get('fatherSurename')
        status = self.request.query_params.get('status')
        prestacion = self.request.query_params.get('prestacion')
        especialidad = self.request.query_params.get('especialidad')

        if firstName is not None and len(firstName) > 3:
            queryset = queryset.filter(firstName__istartswith=firstName)
        if fatherSurename is not None and len(fatherSurename) > 3:
            queryset = queryset.filter(fatherSurename__istartswith=fatherSurename)
        if status is not None:
            queryset = queryset.filter(status=status)            
        if prestacion is not None:
            queryset = queryset.filter(prestaciones__pk__in=prestacion)
        if especialidad is not None:
            queryset = queryset.filter(prestaciones__especialidad__id=especialidad).distinct()
            
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


class ProfesionalDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver del detalle, modificar, o eliminar un Profesional
    """
    serializer_class = ProfesionalNestSerializer
    queryset = Profesional.objects.all()
    permission_classes = (DjangoModelPermissions,)
