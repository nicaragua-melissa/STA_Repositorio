from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.catalogos.animal.API.views import AnimalApiView

router = DefaultRouter()
router.register('', AnimalApiView, basename='Animales')

urlpatterns = [
    path('', AnimalApiView.as_view()),
]