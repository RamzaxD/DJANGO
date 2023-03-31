from django.db import models

# Create your models here.
class Project (models.Model):
    tittle      = models.CharField(max_length=200)
    description = models.TextField()
    created     = models.DateTimeField(auto_now_add=True) #Añade la fecha de ahora de la creacion del post
    update      = models.DateTimeField(auto_now=True) #Obtener la fecha de actualización

    #Para que aparezca con el nombre del titulo el objeto:
    def __str__(self):
        return self.tittle