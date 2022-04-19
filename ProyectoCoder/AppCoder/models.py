from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
          return f"{self.nombre} {self.camada}"

class Estudiantes(models.Model):
     nombre = models.CharField(max_length=30)
     apellido = models.CharField(max_length=30)   
     email = models.EmailField()

     def __str__(self):
          return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
     nombre = models.CharField(max_length=30)
     apellido = models.CharField(max_length=30)   
     email = models.EmailField()
     profesion = models.CharField(max_length=30)

     def __str__(self):
          return f"{self.nombre} {self.apellido}"

class Entregables(models.Model):
     nombre = models.CharField(max_length=30)
     fechaDeEntrega = models.DateField() 
     entregado = models.BooleanField()

     def __str__(self):
          return f"{self.nombre} {self.entregado}"

class Avatar(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE) 
     imagen = models.ImageField(upload_to='avatares', null = True, blank = True)         