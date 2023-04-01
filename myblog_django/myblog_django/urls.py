"""myblog_django URL Configuration

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
from django.contrib     import admin
from django.urls        import path, include
from .                  import views
#from django.http import HttpResponse

#Django settings
from django.conf import settings #importando las configuraciones de django para las image roots
from django.conf.urls.static import static #importando los archivos estaticos

urlpatterns = [
    #BLOG PRINCIPAL PORTADA
    path('',                views.principal, name="portada_principal"),
    
    
    #URLS PARA NUCLEO INCLUYE todo
    path('core_saludo/',     include('core.urls')),
    
    #URLS PARA LA SECCION DE BLOGS
    path('blog_saludo/',     include('blog.urls')),
    
    #URLS PARA LA SECCION DEL PERFIL
    path('perfil_saludo/',   include('perfil.urls')),
    
    #admin
    #para crear super usuario: py .\manage.py createsuperuser
    path('admin/',          admin.site.urls),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #Ruta de Url y archivos estaticos
