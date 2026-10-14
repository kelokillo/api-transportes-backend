from rest_framework import viewsets
from .models import Conductor, Vehiculo, Viaje
from .serializers import ConductorSerializer, VehiculoSerializer, ViajeSerializer
from django.shortcuts import render

# --- IMPORTACIONES NUEVAS PARA SEGURIDAD ---
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# --- VISTAS PÚBLICAS ---
def bienvenida(request):
    return render(request, 'bienvenida.html')

# --- VISTAS PROTEGIDAS ---

# 1. Vista basada en función (FBV) protegida
@login_required
def panel_funciones(request):
    contexto = {'tipo_vista': 'Function Based View (FBV) protegida'}
    return render(request, 'dashboard.html', contexto)

# 2. Vista basada en clase (CBV) protegida
class PanelClases(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_vista'] = 'Class Based View (CBV) protegida'
        return context

# --- VIEWSETS DE LA API REST ---

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer