from django.urls import path
from . import views
urlpatterns = [
    path('', views.saludo, name='saludo_perfil'), 
]
