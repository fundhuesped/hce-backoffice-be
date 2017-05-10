#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_pacientes import views

app_name = "hc_pacientes"
urlpatterns = [
    url(r'^paciente/$', views.PacienteList.as_view(), name='Paciente-list'),
    url(r'^paciente/(?P<pk>[0-9]+)/$', views.PacienteDetails.as_view(), name='Paciente-detail'),
]
