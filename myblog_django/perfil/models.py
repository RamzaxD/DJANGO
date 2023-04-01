from django.db import models
#ckeditor
from ckeditor.fields import RichTextField #importar la biblioteca de ckeditor

# Create your models here. Cada que editamos la class de alguna aplicación hay que migrarla
class Project (models.Model):
    tittle      = models.CharField(max_length=200, verbose_name="Titulo") #maximo de 200 caracteres y aparecera con el nombre de Titulo
    # Sin ckeditor -> description = models.TextField()
    description = RichTextField(verbose_name= 'descripción')#con ckeditor
    created     = models.DateTimeField(auto_now_add=True) #Añade la fecha de ahora de la creacion del post
    update      = models.DateTimeField(auto_now=True) #Obtener la fecha de actualización

    class Meta():
        verbose_name = "Proyectos" #modifica el nombre en el menu de admin 
        verbose_name = "Proyecto" #modifica al seleccionar proyectos en el menu del admin
        ordering = ["-tittle"]#ordenar por titulo predeterminadamente
    #Para que aparezca con el nombre del titulo el objeto:
    def __str__(self):
        return self.tittle