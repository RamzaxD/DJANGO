from django.http import HttpResponse

def principal(request):
    return HttpResponse(f"<h1>Bienvenido a mi blog</h1>")

def post(request, id): #toma el pedido y el id del blog
    return HttpResponse(f'<h2>Post del id...</h2>')