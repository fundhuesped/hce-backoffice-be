"""huesped_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from huesped_backend import views

apps_patterns = ([
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^comun/', include('hc_common.urls')),
    url(r'^pacientes/', include('hc_pacientes.urls')),
    url(r'^core/', include('hc_core.urls')),
    url(r'^masters/', include('hc_masters.urls', namespace='masters')),
    url(r'^hce/', include('hc_hce.urls', namespace='hce'))
])

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^info/', views.info_view.info),
    url(r'^api/', include(apps_patterns, namespace='api')),
]
