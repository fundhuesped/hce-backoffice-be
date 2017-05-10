#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_common import views

app_name = "hc_common"
urlpatterns = [
    url(r'^sexType/$', views.SexTypeList.as_view(), name='SexType-list'),
    url(r'^sexType/(?P<pk>[0-9]+)/$', views.SexTypeDetails.as_view(), name='SexType-detail'),

    url(r'^documentType/$', views.DocumentTypeList.as_view(), name='DocumentType-list'),
    url(r'^documentType/(?P<pk>[0-9]+)/$', views.DocumentTypeDetails.as_view(), name='DocumentType-detail'),

    url(r'^province/$', views.ProvinceList.as_view(), name='Province-list'),
    url(r'^province/(?P<pk>[0-9]+)/$', views.ProvinceDetails.as_view(), name='Province-detail'),

    url(r'^district/$', views.DistrictList.as_view(), name='District-list'),
    url(r'^district/(?P<pk>[0-9]+)/$', views.DistrictDetails.as_view(), name='District-detail'),

    url(r'^location/$', views.LocationList.as_view(), name='Location-list'),
    url(r'^location/(?P<pk>[0-9]+)/$', views.LocationDetails.as_view(), name='Location-detail'),

    url(r'^educationType/$', views.EducationTypeList.as_view(), name='EducationType-list'),
    url(r'^educationType/(?P<pk>[0-9]+)/$', views.EducationTypeDetails.as_view(), name='EducationType-detail'),

    url(r'^civilStatusType/$', views.CivilStatusTypeList.as_view(), name='CivilStatusType-list'),
    url(r'^civilStatusType/(?P<pk>[0-9]+)/$', views.CivilStatusTypeDetails.as_view(), name='CivilStatusType-detail'),

    url(r'^socialService/$', views.SocialServiceList.as_view(), name='SocialService-list'),
    url(r'^socialService/(?P<pk>[0-9]+)/$', views.SocialServiceDetails.as_view(), name='SocialService-detail'),
]
