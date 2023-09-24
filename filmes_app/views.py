from rest_framework import generics
from .models import Filme
from .serializers import FilmeSerializer

class FilmeListCreate(generics.ListCreateAPIView):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer

class FilmeRetrieveDestroy(generics.RetrieveDestroyAPIView):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer