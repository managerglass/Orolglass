from rest_framework import serializers
from .models import Projeto
from backend.imagem.serializers import ImagemSerializer


class ProjetoSerializer(serializers.ModelSerializer):
    imagem = ImagemSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = '__all__'
        