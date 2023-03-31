from django.contrib import admin

#importar tus modelos aquí.
from .models import Project
# Register your models here.
#admin.site.register(Project) #agregar al panel de admin nuestra DB de forma predeterminada

#Para personalizar el admin de nuestra DB:
@admin.register(Project)#decorador del Project.
class PostAdmin(admin.ModelAdmin):#heredando del ModelAdmin    
    list_display = ('id', 'tittle', 'created', 'update')#columnas en la tupla
    list_display_links = ('id','tittle',)#colocarle link al valor 
