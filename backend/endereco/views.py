from rest_framework import generics
from .models import Endereco
from .serializers import EnderecoSerializer


class EnderecoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class EnderecoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
