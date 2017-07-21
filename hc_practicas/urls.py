#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_practicas import views

app_name = "hc_practicas"
urlpatterns = [
    url(r'^profesional/$', views.ProfesionalList.as_view(), name='Profesional-list'),
    url(r'^profesional/(?P<pk>[0-9]+)/$', views.ProfesionalDetails.as_view(), name='Profesional-detail'),
]
