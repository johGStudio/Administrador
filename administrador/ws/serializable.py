from rest_framework import serializers
from gestion.models import alumno, materia

class EstudianteSerializable(serializers.ModelSerializer):
	class Meta:
		model = alumno
		fields = ("cedula","nombre","apellido")

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model = materia 
		fields = ("nombre","cupo")