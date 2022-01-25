from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "App/index.html")

def buscarPersona(request):
    return render(request, "App/buscarPersona.html")

def buscar(request):

    if request.GET["nombre"]:

        mensaje="ey que pasa: %r" %request.GET["nombre"]

        nombre = request.GET["nombre"]

        return render(request, "App/resultadosBusqueda.html", {"nombre":nombre})
    
    else:
        mensaje="Introduce nombre"

    return HttpResponse(mensaje)