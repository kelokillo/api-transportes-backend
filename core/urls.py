"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from taller import views

urlpatterns = [
    # Ruta principal: ahora muestra la página de bienvenida
    path('', views.bienvenida, name='bienvenida'),
    
    # Rutas de Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Vistas Protegidas
    path('panel-fbv/', views.panel_funciones, name='panel_fbv'),
    path('panel-cbv/', views.PanelClases.as_view(), name='panel_cbv'),
    
    # Panel de administración
    path('admin/', admin.site.urls),
    
    # Los endpoints
    path('api/', include('taller.urls')), 
]