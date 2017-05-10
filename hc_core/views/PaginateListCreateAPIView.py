from rest_framework import generics


class PaginateListCreateAPIView(generics.ListCreateAPIView):
    """
    Vista que hereda de ListCreateAPIView y agrega la posibilidad de paginar o no sus resultados
    """

    def initial(self, request, *args, **kwargs):
        all_items = self.request.query_params.get('all')
        # si el valor es true, entonces quiere todos los valores
        if all_items == 'True' or all_items == 'true':
            self.pagination_class = None
        super(PaginateListCreateAPIView, self).initial(request, *args, **kwargs)
