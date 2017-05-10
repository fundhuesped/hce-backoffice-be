from rest_framework.pagination import PageNumberPagination

class ParameterPageNumberPaginator(PageNumberPagination):
    page_size = 5
    max_page_size = 100
    page_size_query_param = 'page_size'