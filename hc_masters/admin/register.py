from django.contrib import admin
from hc_masters.models import Problem
from hc_masters.models import ClinicalStudy
from hc_common.models import SocialService
from hc_masters.models import Vaccine
from hc_masters.models import Medication
from hc_masters.models import MedicationType
from hc_hce.models import Importation, ImportationDeterminationRelationship, ImportationLabRelationship, ImportationPatientRelationship, ImportationRegister



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

class ImportationRegisterAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'name', 'surname', 'birthDate', 'gender', 'documentType', 'documentNumber', 'determination_id', 'determination_version_id', 'determination_description', 'determination_code', 'determination_number', 'lab_Date', 'lab_id', 'processed_patient_id', 'processed_determination_id', 'processed_lab_id', 'fully_processed', 'created_on')
    list_editable = ([])
    list_filter = ([])

class ImportationPatient(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'name', 'surname', 'birthDate', 'gender', 'documentType', 'documentNumber', 'processed_patient_id', 'created_on')
    list_editable = ('patient_id', 'name', 'surname', 'birthDate', 'gender', 'documentType', 'documentNumber', 'processed_patient_id')
    list_filter = ([])

class ImportationDetermination(admin.ModelAdmin):
    list_display = ('id', 'determination_id', 'determination_version_id', 'determination_description', 'determination_code', 'determination_number', 'processed_determination_id', 'created_on')
    list_editable = ('determination_id', 'determination_version_id', 'determination_description', 'determination_code', 'determination_number', 'processed_determination_id')
    list_filter = ([])

class ImportationLaboratory(admin.ModelAdmin):
    list_display = ('id', 'lab_Date', 'lab_id', 'processed_lab_id', 'created_on')
    list_editable = ()
    list_filter = ([])

admin.site.register(Problem, ProblemAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
admin.site.register(ClinicalStudy, ClinicalStudyAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(MedicationType, MedicationTypeAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(Importation, ImportationAdmin)
admin.site.register(ImportationRegister, ImportationRegisterAdmin)
admin.site.register(ImportationPatientRelationship, ImportationPatient)
admin.site.register(ImportationDeterminationRelationship, ImportationDetermination)
admin.site.register(ImportationLabRelationship, ImportationLaboratory)
