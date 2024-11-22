from django.urls import path
from .views import (
    ProjetoListCreateAPIView,
    ProjetoRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'projeto',
        ProjetoListCreateAPIView.as_view(),
        name = 'projeto-list-create-list-api-view'
    ),
    path(
        'projeto/<str:pk>',
        ProjetoRetrieveUpdateAPIView.as_view(),
        name = 'projeto-retrieve-update-api-view'
    )
]