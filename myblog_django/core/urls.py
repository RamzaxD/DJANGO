from django.urls import path, incluede
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('core/', views.core),
]
