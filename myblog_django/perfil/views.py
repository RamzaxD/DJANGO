from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def perfil(resquest):
    return HttpResponse(f'Hola desde mi perfil')
