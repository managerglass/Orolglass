from django.urls import path
from .views import (
    EnderecoListCreateAPIView,
    EnderecoRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'enderecos/',
        EnderecoListCreateAPIView.as_view(),
        name='enderecos-list-create-api-view'
    ),
    path(
        'enderecos/<str:pk>/',
        EnderecoRetrieveUpdateAPIView.as_view(),
        name='enderecos-retrieve-update-api-view'
    ),
]