"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls    import path
from django.http    import HttpResponse #agregar biblioteca para hacer impresion de datos
from .          import views         #importamos la funcion hola desde el modulo de vistas



urlpatterns = [
    path('hola/', views.hola),
    path('verificar/<nombre>/<int:edad>/', views.verificar),
    path('admin/', admin.site.urls),
    
]
