from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Familia

# Create your views here.

def familiar(request, relacion, nombre, edad, cumpleagnos):

    mi_familiar = Familia(relacion = relacion, nombre = nombre, edad = edad, cumpleagnos = cumpleagnos)
    mi_familiar.save()

    miHtml = open('C:/Users/Usuario/Desktop/UBA/Z. Python Coderhouse/proyectoFamilia/projectFamiliaApp/projectFamiliaApp/Plantillas/CreaFamiliar.html')

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
    