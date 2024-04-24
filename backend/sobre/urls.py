from django.urls import path
from .views import (
    SobreListCreateAPIView,
    SobreRetrieveUpdateAPIView
)


urlpatterns = [
    path(
        'sobre/',
        SobreListCreateAPIView.as_view(),
        name='sobre-list-create-api-view'
    ),
    path(
        'sobre/<str:pk>/',
        SobreRetrieveUpdateAPIView.as_view(),
        name='sobre-retrieve-update-api-view'
    )
]
