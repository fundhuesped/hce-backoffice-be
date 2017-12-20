from django.contrib import admin
from hc_masters.models import Problem
from hc_masters.models import ClinicalStudy
from hc_common.models import SocialService
from hc_masters.models import Vaccine
from hc_masters.models import Medication
from hc_masters.models import MedicationType



class ProblemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'status', 'problemType')

class SocialServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'status')

class ClinicalStudyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'status')

class VaccineAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'status')

class MedicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'status')

class MedicationTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'code', 'group')

admin.site.register(Problem, ProblemAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
admin.site.register(ClinicalStudy, ClinicalStudyAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(MedicationType, MedicationTypeAdmin)
admin.site.register(Medication, MedicationAdmin)
