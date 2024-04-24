from rest_framework import serializers
from .models import Destaque
from backend.categoria.serializers import CategoriaSerializer
from backend.imagem.serializers import ImagemSerializer


class DestaqueSerializer(serializers.ModelSerializer):
    tipo = CategoriaSerializer()
    imagem = ImagemSerializer()

    class Meta:
        model = Destaque
        fields = '__all__'
