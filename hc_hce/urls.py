#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_hce import views

app_name = "hc_hce"
urlpatterns = [
    url(r'^visit/(?P<pk>[0-9]+)/$', views.VisitDetails.as_view(), name='Visit-detail'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/visits$', views.PacienteVisitList.as_view(), name='Paciente-Visit-list'),
    url(r'^paciente/(?P<pacienteId>[0-9]+)/currentVisit$', views.CurrentVisitDetail.as_view(), name='Current-Visit-detail'),
]
