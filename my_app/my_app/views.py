#todas las pestañas o vistas de mi pagina web
#hay que importar el modulo a urls para que se muestre

from django.http import HttpResponse #agregar biblioteca para hacer impresion de datos

def hola(request):
    print(request)#contiene el pedido o petición del cliente
    print (request.GET) #Diccionario generado por get que nos manda un diccionario vacio
    num = [int(n) for n in request.GET['numeros'].split(',')] #pasar la key de un diccionario a una lista
    numeros_ordenados = sorted(num)
    print(numeros_ordenados)
    return HttpResponse(str(numeros_ordenados))#colocando en el url ?numeros=1,2,3,4,5 capturamos en una lista los datos
    #return HttpResponse('Hola mundo de DJANGO') #diccionario que retornamos con una cadena de caracteres

def verificar(request, nombre, edad):
    if edad < 18:
        mensaje = f'{nombre} no tienes acceso a la pagina'
    else:
        mensaje = f'Bienvenido {nombre}'
    
    return HttpResponse(mensaje)
