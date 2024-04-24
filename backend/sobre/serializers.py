from rest_framework import serializers
from .models import Sobre
from backend.imagem.serializers import ImagemSerializer


class SobreSerializer(serializers.ModelSerializer):
    imagens =  ImagemSerializer(many=True, read_only=True)

    class Meta:
        model = Sobre
        fields = '__all__'
