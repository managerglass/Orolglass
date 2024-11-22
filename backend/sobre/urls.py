from django.urls import path
from .views import (
    SobreListCreateAPIView,
    SobreRetrieveUpdateAPIView,
    ValoresListCreateAPIView,
    ValoresRetrieveUpdateAPIView,
    CrencasListCreateAPIView,
    CrencasRetrieveUpdateAPIView
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
    ),
    path(
        'valores/',
        ValoresListCreateAPIView.as_view(),
        name='valores-list-create-api-view'
    ),
    path(
        'valores/<str:pk>/',
        ValoresRetrieveUpdateAPIView.as_view(),
        name='valores-retrieve-update-api-view'
    ),
    path(
        'crencas/',
        CrencasListCreateAPIView.as_view(),
        name='crencas-list-create-api-view'
    ),
    path(
        'crencas/<str:pk>/',
        CrencasRetrieveUpdateAPIView.as_view(),
        name='crencas-retrieve-update-api-view'
    ),
]
