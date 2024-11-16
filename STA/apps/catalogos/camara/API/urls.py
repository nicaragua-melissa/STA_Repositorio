from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.catalogos.camara.API.views import CamaraApiView

router = DefaultRouter()
router.register('', CamaraApiView, basename='Camaras')

urlpatterns = [
    path('', CamaraApiView.as_view()),
]
