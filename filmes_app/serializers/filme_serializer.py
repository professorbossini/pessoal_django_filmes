from rest_framework import serializers
#lembre-se de ajustar os imports
from filmes_app.models import Filme
from .genero_serializer import GeneroSerializer

class FilmeSerializer (serializers.ModelSerializer):
  #o nome genero deve ser igual ao nome especificado no modelo de filme
  genero = GeneroSerializer()
  class Meta:
    model = Filme
    fields = '__all__'