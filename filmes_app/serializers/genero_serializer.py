from rest_framework import serializers
#lembre-se de ajustar o import
from filmes_app.models import Genero

class GeneroSerializer (serializers.ModelSerializer):
  class Meta:
    model = Genero
    fields = '__all__'