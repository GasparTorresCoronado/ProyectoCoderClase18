from cgitb import text
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Familiar

# Create your views here.

def familiar(request):
    familiar=Familiar(nombre="Hugo",apellido="Perez",fecha_nacimiento="1990-04-05",estado_civil="Casado",email="hugoperez5@gmail.com",celular="261312567")
    familiar.save()
    texto=f"Familiar Agregado:  NOMBRE: {familiar.nombre}  APELLIDO: {familiar.apellido}  NACIMIENTO: {familiar.fecha_nacimiento}  ESTADO CIVIL: {familiar.estado_civil}  E-mail: {familiar.email} Celular: {familiar.celular}"
    return HttpResponse(texto)
