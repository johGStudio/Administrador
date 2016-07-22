from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'gestion.views.listar'), # r'^$' referencia al index
    url(r'^crearMateria/$', 'gestion.views.crearMateria'),
    url(r'^crearAlumno/$', 'gestion.views.crearAlumno'),
    url(r'^eliminarMateria/$', 'gestion.views.deletemat'),
    
]