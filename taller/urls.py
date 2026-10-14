from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConductorViewSet, VehiculoViewSet, ViajeViewSet

# Creamos el router y registramos nuestras vistas
router = DefaultRouter()
router.register(r'conductores', ConductorViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'viajes', ViajeViewSet)

urlpatterns = [
    # Dejamos la ruta en blanco porque el prefijo 'api/' ya viene de core/urls.py
    path('', include(router.urls)),
]