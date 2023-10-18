from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import  Q

def index(request):
    return render(request, 'index.html')

def raiz (request):
    return redirect('/inicio')

def blog(request):
    return render(request, 'blog.html')