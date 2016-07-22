from django import forms
from .models import alumno
from .models import materia

class FormularioAlumno(forms.ModelForm):
	class Meta:
		model = alumno
		fields= ["cedula","nombre","apellido"]

class FormularioMateria(forms.ModelForm):
	class Meta:
		model = materia
		fields= ["nombre","codigo","cupo"]