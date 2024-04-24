from rest_framework import generics
from .models import Sobre
from .serializers import SobreSerializer


class SobreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer


class SobreRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sobre.objects.all()
    serializer_class = SobreSerializer
