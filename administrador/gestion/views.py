from django.shortcuts import render, redirect
from django.contrib import messages
from .models import alumno
from .models import materia
from .forms import FormularioMateria, FormularioAlumno

# Create your views here.
def listar(request):
	mat = materia.objects.all()
	alum = alumno.objects.all()
	context={
		'mat':mat,
		'alum':alum,
	}
	return render(request,"listar.html",context)

def crearMateria(request):
	f=FormularioMateria(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			dato = f.cleaned_data
			m = materia()
			m.nombre=dato.get("nombre")
			m.codigo=dato.get("codigo")
			m.cupo=dato.get("cupo")
			if(m.save()!=True):
				messages.add_message(request,messages.SUCCESS, "Materia creada!", fail_silently=True)
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"crearMateria.html",context)



def crearAlumno(request):
	f=FormularioAlumno(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			dato = f.cleaned_data
			m = alumno()
			m.cedula=dato.get("cedula")
			m.nombre=dato.get("nombre")
			m.apellido=dato.get("apellido")
			if(m.save()!=True):
				messages.add_message(request,messages.SUCCESS, "Materia creada!", fail_silently=True)
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"crearAlumno.html",context)

def deletealum(request):
	alumno=alumno.objects.filter(cedula=request.GET["cedula"])
	alumno.delete()
	
	return redirect(listar)

def deletemat(request):
	mat=materia.objects.filter(codigo=request.GET["codigo"])
	if(mat.delete()!=True):
		messages.add_message(request,messages.WARNING, "Materia Eliminada!", fail_silently=True)
	return redirect(listar)

