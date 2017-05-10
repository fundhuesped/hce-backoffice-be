from rest_framework.exceptions import APIException

class FailedDependencyException(APIException):
    status_code = 424
    default_detail = 'Failed dependency'