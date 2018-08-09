from django.contrib import admin
from hc_masters.models import Problem
from hc_masters.models import ClinicalStudy
from hc_common.models import SocialService
from hc_masters.models import Vaccine
from hc_masters.models import Medication
from hc_masters.models import MedicationType



class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'problemType', 'problemTypeTmp')
    list_editable = ('name', 'description', 'status', 'problemType', 'problemTypeTmp')
    search_fields = ['name',]
    list_filter = ('problemType', 'problemTypeTmp', 'status')

class SocialServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status')
    list_editable = ('name', 'description', 'status')
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
    list_editable = ('id', 'name', 'status','medicationType')
    search_fields = ['name']
    list_filter = ('medicationType', 'status')

class MedicationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'group')
    list_editable = ('name', 'code', 'group')
    list_filter = ('group',)

admin.site.register(Problem, ProblemAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
admin.site.register(ClinicalStudy, ClinicalStudyAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(MedicationType, MedicationTypeAdmin)
admin.site.register(Medication, MedicationAdmin)
