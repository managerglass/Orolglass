from rest_framework import generics, filters
from .models import Evento
from .serializers import EventoSerializer


class EventoFilterBackend(filters.BaseFilterBackend):
    def  filter_queryset(self, request, queryset, view):
        tipo = request.query_params.get('tipo', None)
        titulo = request.query_params.get('titulo', None)
        data = request.query_params.get('data', None)

        filters = {}

        if tipo:
            filters['tipo__nome__icontains'] = tipo
        if titulo:
            filters['titulo__icontains'] = titulo
        if data:
            filters['data'] = data
        
        return queryset.filter(**filters)


class EventoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [EventoFilterBackend]


class EventoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer