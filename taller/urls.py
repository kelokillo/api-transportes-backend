from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConductorViewSet, VehiculoViewSet, ViajeViewSet

# Creamos el router y registramos nuestras vistas
router = DefaultRouter()
router.register(r'conductores', ConductorViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'viajes', ViajeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]