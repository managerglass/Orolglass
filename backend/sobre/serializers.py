from rest_framework import serializers
from .models import Sobre, Valores, Crencas
from backend.imagem.serializers import ImagemSerializer
    

class SobreSerializer(serializers.ModelSerializer):
    imagens =  ImagemSerializer(many=True, read_only=True)

    class Meta:
        model = Sobre
        fields = '__all__'


class  ValoresSerializer(serializers.ModelSerializer):
    sobre = SobreSerializer()
    class Meta:
        model = Valores
        fields = '__all__'


class  CrencasSerializer(serializers.ModelSerializer):
    sobre = SobreSerializer()
    class Meta:
        model = Crencas
        fields = '__all__'
