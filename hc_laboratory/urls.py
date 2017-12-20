#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_laboratory import views

app_name = "hc_laboratory"
urlpatterns = [
    url(r'^paciente/(?P<pacienteId>[0-9]+)/labResults$', views.PatientLabResults.as_view(), name='Paciente-LaboratoryResult-list'),
    url(r'^determinaciones/(?P<pk>[0-9]+)$', views.DeterminacionDetails.as_view(), name='Determinacion-detail'),
    url(r'^determinaciones/$', views.DeterminacionList.as_view(), name='Determinacion-list')
]
