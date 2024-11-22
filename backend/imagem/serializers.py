from rest_framework import serializers
from .models import Imagem
from backend.categoria.serializers import CategoriaSerializer

class ImagemSerializer(serializers.ModelSerializer):
    tipo = CategoriaSerializer()

    class Meta:
        model = Imagem
        fields = '__all__'
        