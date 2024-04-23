from django.urls import path
from .views import (
    AvaliacaoListCreateAPIView,
    AvaliacaoRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'avaliacoes/',
        AvaliacaoListCreateAPIView.as_view(),
        name='avalizao-list-create-api-view'
    ),
    path(
        'avaliacoes/<str:pk>/',
        AvaliacaoRetrieveUpdateAPIView.as_view(),
        name=('avaliacao-retrieve-update-api-view')
    )
]