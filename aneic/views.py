from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import  Q

def index(request):
    portada = Portada.objects.all()
    sobre_aneic = Sobre_aneic.objects.all()
    pregunta = Preguntas_frecuentes.objects.all()
    miembro = Miembro.objects.all()
    context = {"portada" : portada, "sobre_aneic" : sobre_aneic, "pregunta" : pregunta, "miembro" : miembro}
    return render(request, 'index.html', context)

def raiz (request):
    return redirect('/inicio')

def blog(request):
    return render(request, 'blog.html')


