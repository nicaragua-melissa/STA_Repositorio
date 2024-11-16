from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.catalogos.rutaCritica.API.views import RutaCriticaApiView, RutaCriticaDetails

urlpatterns = [
    path('', RutaCriticaApiView.as_view()),
    path('<int:pk>', RutaCriticaDetails.as_view()),
]