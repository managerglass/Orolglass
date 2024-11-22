from rest_framework import generics, filters
from .models import Categoria
from .serializers import CategoriaSerializer


class CategoriaFilterBackend(filters.BaseFilterBackend):
    def  filter_queryset(self, request, queryset, view):
        nome = request.query_params.get('nome', None)
        tipo = request.query_params.get('tipo', None)

        filters = {}

        if nome:
            filters['nome'] = nome
        if tipo:
            filters['tipo'] = tipo
        
        return queryset.filter(**filters)


class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [CategoriaFilterBackend]


class CategoriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
