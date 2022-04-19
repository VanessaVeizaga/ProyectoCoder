
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from .forms import CursoFormulario, ProfesorFormulario
from .models import Curso, Profesor, Avatar

login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "inicio.html", {"url":avatares[0].imagen.url})

# def curso(request):
#     return render(request, "curso.html")

def profesor(request):
    if request.method == "POST":  
       miFormulario = ProfesorFormulario(request.POST)
       if miFormulario.is_valid():
           informacion = miFormulario.cleaned_data
           
           profesor = Profesor(nombre=informacion["nombre"],
                               apellido=informacion["apellido"],
                               email=informacion["email"],
                               profesion=informacion["profesion"],)
           profesor.save()
           return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario()   
    return render(request, "profesor.html", {"miFormulario": miFormulario})   

def estudiantes(request):
    return render(request, "estudiantes.html")    

def entregables(request):
    return render(request, "entregables.html")

def curso(request):
   # print(request.POST)
    if request.method == "POST":
        
       miFormulario = CursoFormulario(request.POST)
       print(miFormulario)
       if miFormulario.is_valid:
           informacion = miFormulario.cleaned_data
           print(informacion)
           curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
           curso.save()
           return render(request, "inicio.html")
    else:
        miFormulario = CursoFormulario()   
    return render(request, "curso.html", {"miFormulario": miFormulario})    
  
def busquedaCamada(request):
    return render(request, "busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:        
        respuesta = f"Estoy buscando la camada nro.:{request.GET['camada']}"   
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains = camada)
        return render(request, "resultadoBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
      respuesta = "No enviaste datos"
      return HttpResponse(respuesta) 

def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "leerProfesores.html", contexto)   

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre = profesor_nombre)
    profesor.delete()
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre = profesor_nombre)
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion["nombre"]
            profesor.apellido = informacion["apellido"]
            profesor.email = informacion["email"]
            profesor.profesion = informacion["profesion"]
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario(initial={"nombre": profesor.nombre, 
                                                   "apellido" : profesor.apellido,
                                                   "email": profesor.email,
                                                   "profesion": profesor.profesion })
    return render(request, "profesor.html", {"miFormulario": miFormulario})                                               

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "cursos_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "cursos_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "camada"]

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "camada"]    

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user is not None:
                login(request,user)
                return render(request, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje": "Error, datos incorrectos."})
        else:
            return render(request, "inicio.html", {"mensaje": "Error, formulario erróneo."})
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})     

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje": "Usuario creado"})
    else:
        form = UserRegisterForm()
    return render(request, "registro.html", {"form": form})      

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]
            usuario.save()
            return render(request, "inicio.html")
    else:
        miFormulario = UserEditForm(initial = {"email": usuario.email})       
    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})      
            

