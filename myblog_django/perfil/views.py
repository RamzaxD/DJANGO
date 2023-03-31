from django.shortcuts import render
from django.http import HttpResponse

#modelos
from .models import Project

# Create your views here.
def saludo(request):
    #Generar registros en la base de datos
    #project1 = Project(tittle = "Proyecto 1", description = "Este proyecto abarca sobre weas")#Generando un objeto
    #project1.save()#Guardar el objeto en la base de datos

    #project2 = Project(tittle = "Proyecto 2", description = "Este proyecto abarca sobre weas2")#Generando un objeto
    #project2.save()#Guardar el objeto en la base de datos

    #project3 = Project(tittle = "Proyecto 1", description = "Este proyecto abarca sobre weas3",)#Generando un objeto
    #project3.save()#Guardar el objeto en la base de datos
    
    projects = Project.objects.all()
    #projects.delete()#borrar contenido
    print (projects)
    #return HttpResponse(projects)
    return HttpResponse(projects.values())
