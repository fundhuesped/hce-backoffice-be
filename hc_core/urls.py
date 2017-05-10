#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from hc_core import views

app_name = "hc_core"
urlpatterns = [
    url(r'^user/login/$', views.UserLogin.as_view(), name='User-login'),
    url(r'^user/logout/$', views.UserLogout.as_view(), name='User-logout'),
    url(r'^user/change-password/$', views.PasswordChangeView.as_view(), name='Password-Change'),
]
