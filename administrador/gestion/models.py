from django.db import models

class alumno(models.Model):
	cedula = models.CharField(max_length=10, unique=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)

	def __str_(self):
		return self.cedula

class materia(models.Model):
	nombre = models.CharField(max_length=30)
	codigo = models.CharField(max_length=8, unique=True)
	cupo = models.IntegerField(default=0)

	def __str__(self):
		return self.codigo

