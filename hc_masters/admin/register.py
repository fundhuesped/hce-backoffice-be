from django.contrib import admin
from hc_masters.models import Problem
from hc_masters.models import ClinicalStudy
from hc_common.models import SocialService



class ProblemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'status', 'problemType')

class SocialServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'status')
class ClinicalStudyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'status')


admin.site.register(Problem, ProblemAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
admin.site.register(ClinicalStudy, ClinicalStudyAdmin)
