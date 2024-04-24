from rest_framework import serializers
from .models import Evento
from backend.categoria.serializers import CategoriaSerializer
from backend.imagem.serializers import ImagemSerializer


class EventoSerializer(serializers.ModelSerializer):
    tipo = CategoriaSerializer
    imagens = ImagemSerializer(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = '__all__'
