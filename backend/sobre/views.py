from rest_framework import generics
from .models import Sobre, Valores, Crencas
from .serializers import (
    SobreSerializer,
    ValoresSerializer,
    CrencasSerializer
)


class SobreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer


class SobreRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer


class ValoresListCreateAPIView(generics.ListCreateAPIView):
    queryset = Valores.objects.all()
    serializer_class = ValoresSerializer


class ValoresRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Valores.objects.all()
    serializer_class = ValoresSerializer


class CrencasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Crencas.objects.all()
    serializer_class = CrencasSerializer


class CrencasRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Crencas.objects.all()
    serializer_class = CrencasSerializer
