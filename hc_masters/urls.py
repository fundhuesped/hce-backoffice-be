#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_masters import views

app_name = "hc_masters"
urlpatterns = [
    url(r'^problem/$', views.ProblemList.as_view(), name='Problem-list'),
    url(r'^problem/(?P<pk>[0-9]+)/$', views.ProblemDetails.as_view(), name='Problem-details'),
    url(r'^vaccine/$', views.VaccineList.as_view(), name='Vaccine-list'),
    url(r'^vaccine/(?P<pk>[0-9]+)/$', views.VaccineDetails.as_view(), name='Vaccine-details'),
    url(r'^medication/$', views.MedicationList.as_view(), name='Medication-list'),
    url(r'^medication/(?P<pk>[0-9]+)/$', views.MedicationDetails.as_view(), name='Medication-details'),
    url(r'^clinicalStudy/$', views.ClinicalStudyList.as_view(), name='ClinicalStudy-list'),
    url(r'^clinicalStudy/(?P<pk>[0-9]+)/$', views.ClinicalStudyDetails.as_view(), name='ClinicalStudy-details'),
]
