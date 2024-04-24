from rest_framework import generics, filters
from .models import Imagem
from .serializers import ImagemSerializer


class ImagemFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        titulo = request.query_params.get('titulo', None)
        arquivo = request.query_params.get('arquivo', None)
        tipo = request.query_params.get('tipo', None)

        filters = {}

        if titulo:
            filters['titulo'] = titulo
        if arquivo:
            filters['arquvo'] = arquivo
        if tipo:
            filters['tipo__nome__icontains'] = tipo

        return queryset.filter(**filters)
    

class ImagemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    filter_backend = [ImagemFilterBackend]


class ImagemRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    