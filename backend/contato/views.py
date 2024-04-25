from rest_framework import generics, filters
from .models import Contato
from .serializers import ContatoSerializer


class ContatoFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        titulo = request.query_params.get('titulo', None)
        contato = request.query_params.get('contato', None)

        filters = {}

        if titulo:
            filters['titulo__icontains'] = titulo
        if contato:
            filters['contato__icontains'] = contato
        
        return queryset.filter(**filters)


class ContatoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [ContatoFilterBackend]


class ContatoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
