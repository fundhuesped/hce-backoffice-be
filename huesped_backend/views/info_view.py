from rest_framework.decorators import api_view
from rest_framework.response import Response
import django
from django.apps import apps
from huesped_backend import settings
import pip


@api_view(['GET'])
def info(request):
    for app in apps.get_app_configs():
        print(vars(app))

    infoReponse = {
        'dependencies': settings.DEPENDENCIES_INFO,
        'git': settings.GIT_INFO if settings.GIT_INFO is not None else 'Not available'
    }

    return Response(infoReponse)
