from django.urls import path
from apps.movimientos.Denuncia.API.views import DenunciaApiView,DenunciaDetailApiView

app_name = "Denuncia"
urlpatterns = [
    path('', DenunciaApiView.as_view(), name='Denuncias'),                 # Lista de denuncias
    path('<int:pk>/', DenunciaDetailApiView.as_view(), name='denuncia-detail'),  # Detalle de una denuncia específica
]
