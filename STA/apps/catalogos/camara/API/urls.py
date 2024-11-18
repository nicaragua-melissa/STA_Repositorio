from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.catalogos.camara.API.views import CamaraApiView, CamaraDetails

router = DefaultRouter()
router.register('', CamaraApiView, basename='Camaras')

urlpatterns = [
    path('', CamaraApiView.as_view()),
    path('<int:pk>', CamaraDetails.as_view()),
]