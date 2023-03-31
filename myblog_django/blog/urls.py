from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.saludo, name = 'saludo_blog'),
    path('<int:id>',       views.post,      name='post'),
]