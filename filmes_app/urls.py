from django.urls import path
from . import views

urlpatterns = [
  path ('filmes/', views.FilmeListCreate.as_view(), name="filme-list-create"),
  path('filmes/<int:pk>', views.FilmeRetrieveDestroy.as_view(), name='filme-retrieve-destroy')
]