from django.shortcuts import render
from datetime import datetime
from inicio.models import Auto

from django.http import HttpResponse
from django.template import Template, Context, loader
import random

def inicio(request):
    # return HttpResponse('Bienvenidos a mi inicio')
    return render(request, 'inicio/index.html')


def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi Template 1 </h1> <h3>Fecha: {fecha}</h3>  Hola {nombre} {apellido} {edad}')

# --------------------------------------------------------------------------------------------------------------------

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r'C:\Users\rafad\OneDrive\Escritorio\programacion\mi-proyecto\templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    
    fecha = datetime.now()

    datos = {
        'fecha': fecha,
        'nombre': nombre, 
        'apellido': apellido,
        'edad': edad,
        }
    
    contexto = Context(datos)
    
    template_render = template.render(contexto)
    
    return HttpResponse(template_render)

# -------------------------------------------------------------------------------------------

def template3(request, nombre, apellido, edad):
    
    # archivo_abierto = open(r'C:\Users\rafad\OneDrive\Escritorio\programacion\mi-proyecto\templates\template2.html')
    
    # template = Template(archivo_abierto.read())
    
    # archivo_abierto.close()
    
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()

    datos = {
        'fecha': fecha,
        'nombre': nombre, 
        'apellido': apellido,
        'edad': edad,
        }
    
    # contexto = Context(datos) 
    
    template_render = template.render(datos)
    
    return HttpResponse(template_render)

# --------------------------------------------------------------------------------------------------------------------

def template4(request, nombre, apellido, edad):
    
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()

    datos = {
        'fecha': fecha,
        'nombre': nombre, 
        'apellido': apellido,
        'edad': edad,
        }
    
    template_render = template.render(datos)
    
    return render(request, 'template2.html', datos)

# --------------------------------------------------------------------------------------------------------------

def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    print(numeros)
    return render(request, 'probando_if_for.html', {'numeros': numeros})


def crear_auto(request, marca, modelo):
    auto = Auto(marca=marca, modelo=modelo)
    auto.save()
    return render(request, 'auto_templates/creacion.html',{'auto': auto})