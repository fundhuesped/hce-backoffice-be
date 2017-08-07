from django.contrib import admin
from hc_masters.models import Problem
from hc_common.models import SocialService



class ProblemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'status', 'problemType')

class SocialServiceAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'status')


admin.site.register(Problem, ProblemAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
