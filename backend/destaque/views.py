from rest_framework import generics, filters
from .models import Destaque
from .serializers import DestaqueSerializer


class DestaqueFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        tipo = request.query_params.get('tipo', None)
        titulo = request.query_params.get('titulo', None)

        filters = {}

        if tipo:
            filters['tipo__tipo__icontains'] = tipo
        if titulo:
            filters['titulo__icontains'] = titulo
        
        return queryset.filter(**filters)


class DestaqueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destaque.objects.all()
    serializer_class = DestaqueSerializer
    filter_backends = [DestaqueFilterBackend]


class DestaqueRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Destaque.objects.all()
    serializer_class = DestaqueSerializer
