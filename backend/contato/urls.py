from django.urls import path
from .views import (
    ContatoListCreateAPIView,
    ContatoRetrieveUpdateAPIView
)

urlpatterns = [
    path(
        'contatos/',
        ContatoListCreateAPIView.as_view(),
        name='contatos-list-create-api-view'
    ),
    path(
        'contatos/<str:pk>/',
        ContatoRetrieveUpdateAPIView.as_view(),
        name='contatos-retrieve-update-api-view'
    )
]