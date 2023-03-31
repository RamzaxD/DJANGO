from django.http import HttpResponse

def principal(request):
    return HttpResponse(f"<h1>Bienvenido a mi blog</h1>")

