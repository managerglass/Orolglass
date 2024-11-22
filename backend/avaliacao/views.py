from rest_framework import generics, filters
from .models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        nome = request.query_params.get('nome', None)
        rede_social = request.query_params.get('rede_social', None)

        filters = {}

        if nome:
            filters['nome'] = nome
        if rede_social:
            filters['rede_social'] = rede_social
        
        return queryset.filter(**filters)


class AvaliacaoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    filter_bakcends = [AvaliacaoFilterBackend]


class AvaliacaoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
