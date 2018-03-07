#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import generics, filters
from rest_framework.permissions import DjangoModelPermissions
from hc_hce.serializers import PatientARVPrescriptionNestSerializer

from hc_hce.models import PatientARVPrescription


class PatientARVPrescriptionDetail(generics.RetrieveAPIView):
    serializer_class = PatientARVPrescriptionNestSerializer
    queryset = PatientARVPrescription.objects.all()
    # permission_classes = (DjangoModelPermissions,)
