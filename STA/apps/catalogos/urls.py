from django.urls import path, include

urlpatterns = [
    path('animales/', include('apps.catalogos.animal.API.urls')),
    path('camaras/', include('apps.catalogos.camara.API.urls')),
    path('rutas/', include('apps.catalogos.rutaCritica.API.urls')),
]