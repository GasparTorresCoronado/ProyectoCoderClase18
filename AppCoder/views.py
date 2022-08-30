from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar
# Create your views here.

def familiar(request):
    familiar=Familiar(nombre="Camila",apellido="Perez",fecha_nacimiento="1993-05-24",estado_civil="Casada",email="camiperez@hotmail.com",celular="2615672190")
    familiar.save()
    texto=f"Familiar Agregado:  NOMBRE: {familiar.nombre}  APELLIDO: {familiar.apellido}  NACIMIENTO: {familiar.fecha_nacimiento}  ESTADO CIVIL: {familiar.estado_civil}  E-mail: {familiar.email} Celular: {familiar.celular}"
    return HttpResponse(texto)

def familiar_detalles(request):
    fam= Familiar.objects.get(id=1)
    fam2= Familiar.objects.get(id=2)
    fam3= Familiar.objects.get(id=3)
    context= {
        'nombre1': fam.nombre,
        'apellido1': fam.apellido,
        'fecha_nacimiento1':fam.fecha_nacimiento,
        'estado_civil1':fam.estado_civil,
        'email1':fam.email,
        'celular1':fam.celular,
        'nombre2':fam2.nombre,
        'apellido2': fam2.apellido,
        'fecha_nacimiento2':fam2.fecha_nacimiento,
        'estado_civil2':fam2.estado_civil,
        'email2':fam2.email,
        'celular3':fam2.celular,
        'nombre3':fam3.nombre,
        'apellido3': fam3.apellido,
        'fecha_nacimiento3':fam3.fecha_nacimiento,
        'estado_civil3':fam3.estado_civil,
        'email3':fam3.email,
        'celular3':fam3.celular,
        }
    return render(request, "C:/Programacion/Proyecto1/ProyectoCoder/ProyectoCoder/Plantillas/template1.html", context)