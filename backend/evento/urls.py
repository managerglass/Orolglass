from django.urls import path
from .views import (
    EventoListCreateAPIView,
    EventoRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'eventos/',
        EventoListCreateAPIView.as_view(),
        name='evento-list-create-api-view'
    ),
    path(
        'eventos/<str:pk>/',
        EventoRetrieveUpdateAPIView.as_view(),
        name='evento-retrieve-update-api-view'
    )
]