from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def curso(request):
    curso = Curso(nombre = "Pyhton", camada = 19881)
    curso.save()
    documentoDeTexto = f"---> Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)
