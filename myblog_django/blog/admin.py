from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)

@admin.register (Post)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'image')
    list_display_links = ('id','tittle', "image")#colocarle link al valor para que vaya directamente ala consulta