#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_masters import views

app_name = "hc_masters"
urlpatterns = [
    url(r'^problem/$', views.ProblemList.as_view(), name='Problem-list'),
    url(r'^problem/(?P<pk>[0-9]+)/$', views.ProblemDetails.as_view(), name='Problem-detail'),
]
