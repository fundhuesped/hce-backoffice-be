#!/usr/bin/python
# -*- coding: utf-8 -*-

# from django.conf.urls import url
# from django.contrib import admin
# from django.template.response import TemplateResponse
# from hc_hce.models import Visit

# @admin.register(Visit)
# class ImportationAdmin(admin.ModelAdmin):

#     def get_urls(self):

#         # get the default urls
#         urls = super(ImportationAdmin, self).get_urls()

#         # define security urls
#         custom_urls = [
#             url(r'^importacion$', self.admin_site.admin_view(self.importacion_view))
#             # Add here more urls if you want following same logic
#         ]

#         # Make sure here you place your added urls first than the admin default urls
#         return custom_urls + urls

#     # Your view definition fn
#     def importacion_view(self, request):
#         context = dict(
#             self.admin_site.each_context(request), # Include common variables for rendering the admin template.
#             something="test",
#         )
#         return TemplateResponse(request, "importacion.html", context)

# class CustomAdminSite(admin.AdminSite):
  
#     def get_urls(self):
#         urls = super(CustomAdminSite, self).get_urls()
#         custom_urls = [
#             url(r'desired/path$', self.admin_view(organization_admin.preview), name="preview"),
#         ]
#         return urls + custom_urls