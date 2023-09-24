from rest_framework import generics
#ajuste os imports
from filmes_app.models import Filme
from filmes_app.serializers import FilmeSerializer

class FilmeListCreate(generics.ListCreateAPIView):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer

class FilmeRetrieveDestroy(generics.RetrieveDestroyAPIView):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer