from django.urls import path
from .views import (
    DestaqueListCreateAPIView,
    DestaqueRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'destaques/',
        DestaqueListCreateAPIView.as_view(),
        name='destaques-list-create-api-view'
    ),
    path(
        'destaques/<str:pk>/',
        DestaqueRetrieveUpdateAPIView.as_view(),
        name='destaques-retrieve-update-api-view'
    )
]
