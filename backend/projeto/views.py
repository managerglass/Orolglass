from rest_framework import generics, filters
from .models import Projeto
from .serializers import ProjetoSerializer


class ProjetoFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        titulo = request.query_params.get('titulo', None)
        tipo = request.query_params.get('tipo', None)
        

        filters = {}

        if titulo:
            filters['titulo'] = titulo
        if tipo:
            filters['descricao'] = tipo

        return queryset.filter(**filters)
    

class ProjetoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    filter_backend = [ProjetoFilterBackend]


class ProjetoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
