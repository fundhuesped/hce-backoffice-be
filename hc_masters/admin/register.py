from django.contrib import admin
from hc_masters.models import Problem
from hc_masters.models import ClinicalStudy
from hc_common.models import SocialService
from hc_masters.models import Vaccine
from hc_masters.models import Medication
from hc_masters.models import MedicationType
from hc_hce.models import Importation



class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'problemType', 'problemTypeTmp')
    list_editable = ('name', 'description', 'status', 'problemType', 'problemTypeTmp')
    search_fields = ['name',]
    list_filter = ('problemType', 'problemTypeTmp', 'status')

class SocialServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'order', 'status')
    list_editable = ('name', 'description', 'order', 'status')
    search_fields = ['name',]
    list_filter = ('status',)

class ClinicalStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'synonym')
    list_editable = ('name', 'status', 'synonym')
    search_fields = ['name',]
    list_filter = ('status',)

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'synonym')
    list_editable = ('name', 'status', 'synonym')
    search_fields = ['name']
    list_filter = ('status',)

class MedicationAdmin(admin.ModelAdmin):

    fieldsets = ( (None, {'fields' : ('name', 'status', 'medicationType')}),
                    ('Solo ARV', { 
                        'classes': ('collapse',),
                        'fields':('composition', 'presentation', 'abbreviation')}
                    ),
                )
    list_display = ('id', 'name', 'status','medicationType')
    list_editable = ('name', 'status','medicationType')
    search_fields = ['name']
    list_filter = ('medicationType', 'status')
    list_display_links = list(('id', ))

class MedicationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'group')
    list_editable = ('name', 'code', 'group')
    list_filter = ('group',)


class ImportationAdmin(admin.ModelAdmin):
    list_display = ('id', 'csv', 'created')
    list_editable = ([])
    list_filter = ([])

admin.site.register(Problem, ProblemAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
admin.site.register(ClinicalStudy, ClinicalStudyAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(MedicationType, MedicationTypeAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Importation, ImportationAdmin)
