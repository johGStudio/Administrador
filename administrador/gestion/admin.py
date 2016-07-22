from django.contrib import admin
from .models import alumno
from .models import materia

# Register your models here.
class AdminAlumno(admin.ModelAdmin):
	list_display = ["__str__","cedula","nombre","apellido"]
	class Meta:
		model = alumno
admin.site.register(alumno,AdminAlumno)

class AdminMateria(admin.ModelAdmin):
	list_display = ["__str__","nombre","codigo","cupo"]
	class Meta:
		model = materia
admin.site.register(materia,AdminMateria)