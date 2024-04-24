from django.urls import path
from .views import (
    ImagemListCreateAPIView,
    ImagemRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'imagem/',
        ImagemListCreateAPIView.as_view(),
        name = 'imagem-list-create-api-view'
    ),
    path(
        'imagem/<str:pk>/',
        ImagemRetrieveUpdateAPIView.as_view(),
        name = 'imagem-retrieve-update-api-view'
    )
]
