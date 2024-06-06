from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Bienvenidos a mi inicio')


def template1(request):
    return HttpResponse('Mi Template 1')