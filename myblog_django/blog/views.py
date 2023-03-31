from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def saludo(request):
    #blog1 = Post(tittle = "BLOG 4", description = "lslalalalaa")
    #blog1.save()
    
    posteo = Post.objects.all() #la clase los guarda como una lista
    #posteo.delete()
    post_numero = 0
    total_post = len(posteo)
    print(f"total de post que hay: {total_post}")
    for post_numero in range(total_post):
        print(f"este es el Objeto post: {posteo[post_numero]}")
        print(f"Nombre: {(posteo[post_numero].tittle)}")
        print(f"id: {(posteo[post_numero].id)} ")
    #return HttpResponse(posteo[0].tittle)#muestra titulo del post que se encuentra en el lugar 0 de la lista de objetos
    #print (Post.objects.all()) #Muestra los objetos de la lista
    #posteo = [int(n) for n in range (posteo).split(',')]
    return HttpResponse(posteo)

def post(request, id): #toma el pedido y el id del blog
    posteo = Post.objects.get(id = id)
    content = f'{posteo.tittle} - {posteo.description}'
    return HttpResponse(content)
    #return HttpResponse(f'<h2>Post del id...</h2>')
