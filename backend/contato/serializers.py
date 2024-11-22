from rest_framework import serializers
from .models import Contato
from backend.categoria.serializers import CategoriaSerializer


class ContatoSerializer(serializers.ModelSerializer):
    tipo = CategoriaSerializer()

    class Meta():
        model = Contato
        fields = '__all__'
