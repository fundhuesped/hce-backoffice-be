from background_task import background
from hc_hce.models import Visit


@background(schedule=1800)
def schedule_close(visit_id):
    visit = Visit.objects.get(pk=visit_id)
    if visit.state == Visit.STATE_OPEN:
    	visit.state = Visit.STATE_CLOSED
    	visit.save()