from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('curso', views.curso, name="Curso"),
    path('profesor', views.profesor, name="Profesor"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
#   path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar', views.buscar, name="Buscar"),    
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor, name="EditarProfesor"),
    path('curso/list', views.CursoList.as_view(), name="List"),
    path('curso/detalle/<pk>', views.CursoDetalle.as_view(), name="Detail"),
    path('curso/nuevo', views.CursoCreacion.as_view(), name="New"),
    path('curso/editar/<pk>', views.CursoUpdate.as_view(), name="Edit"),
    path('curso/delete/<pk>', views.CursoDelete.as_view(), name="Delete"),  
    path('login', views.login_request, name="Login"),   
    path('register', views.register, name="Register"), 
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name="Logout"), 
    path('editarPerfil', views.editarPerfil, name="EditarPerfil")

]