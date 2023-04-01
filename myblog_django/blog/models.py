from django.db import models

# Create your models here.
class Post(models.Model): #Generando una clase con herencia de una clase. En el archivo models, tomaremos la clase Model
    #Atributos de mi clase heredados para mi base de datos de POSTS
    image       = models.ImageField(verbose_name="Imagen", upload_to="blog/") #se guardara la imagen en media dentro de una carpeta llamada blog
    tittle      = models.CharField(max_length=200) #maximo de caracteres
    description = models.TextField()
    content     = models.TextField()
    created     = models.DateTimeField(auto_now_add=True) #Añade la fecha de ahora de la creacion del post
    update      = models.DateTimeField(auto_now=True) #Obtener la fecha de actualización

#Para que aparezca con el nombre del titulo el objeto:
    def __str__(self):
        return self.tittle