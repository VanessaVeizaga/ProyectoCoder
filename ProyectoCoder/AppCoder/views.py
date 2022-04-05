from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def inicio(request):
    return render(request, "inicio.html")

def curso(request):
    return render(request, "curso.html")

def profesor(request):
    return render(request, "profesor.html")

def estudiantes(request):
    return render(request, "estudiantes.html")    

def entregables(request):
    return render(request, "entregables.html")

def cursoFormulario(request):
    print(request.POST)
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
        curso.save()
        return render(request, "inicio.html")
    return render(request, "cursoFormulario.html")    
  
