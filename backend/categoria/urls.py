from django.urls import path
from .views import (
    CategoriaListCreateAPIView,
    CategoriaRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'categoria/',
        CategoriaListCreateAPIView.as_view(),
        name='categoria-list-create-api-view'
    ),
    path(
        'categoria/<str:pk>/',
        CategoriaRetrieveUpdateAPIView.as_view(),
        name='categoria-retrieve-update-api-view'
    )
]
