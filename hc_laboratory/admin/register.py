from django.contrib import admin
from hc_laboratory.models import *



class CategoriaDeterminacionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status')
    list_editable = ('name', 'description', 'status')

class DeterminacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'label', 'description', 'unitOfMeasure', 'status', 'category')
    list_editable = ('code', 'label', 'description', 'unitOfMeasure', 'status', 'category')


admin.site.register(CategoriaDeterminacion, CategoriaDeterminacionAdmin)
admin.site.register(Determinacion, DeterminacionAdmin)
