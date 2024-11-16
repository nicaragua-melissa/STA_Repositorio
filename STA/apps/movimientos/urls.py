from django.urls import path, include
from apps.movimientos.Denuncia.API.views import DenunciaApiView

urlpatterns = [
    path('denuncias/', include('apps.movimientos.Denuncia.API.urls')),
]