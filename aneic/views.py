from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import  Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    portada = Portada.objects.all()
    sobre_aneic = Sobre_aneic.objects.all()
    pregunta = Preguntas_frecuentes.objects.all()
    miembro = Miembro.objects.all()
    posts = Post.objects.all().order_by('-published_date')
    convenio = Convenio.objects.all()
    dato = Datos.objects.all()
    precio = Precio.objects.all()
    preciopro = Preciopro.objects.all()
    contacto = Contacto.objects.all()
    context = {"portada" : portada, "sobre_aneic" : sobre_aneic, "pregunta" : pregunta, "miembro" : miembro, "posts" : posts, "convenio" : convenio, "dato" : dato, "precio" : precio, "preciopro" : preciopro, "contacto" : contacto,}
    return render(request, 'index.html', context)

def raiz (request):
    return redirect('/inicio')

def blog (request):
    posts = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paginator_posts = paginator.get_page(page)
    posts = Post.objects.all().order_by('-published_date')[0:6]
    contexto = {"posts_pagin": paginator_posts, "posts": posts}
    return render(request, 'blog.html', contexto)

def single_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts = Post.objects.all().order_by('-published_date')[0:6]
    contexto = {"post": post, "posts":posts}
    return render(request, 'blog-single.html', contexto)

def home(request):
    return render(request, 'core/home.html')

def membresia(request):
    return render(request, 'membership.html')

def comisiondirectiva(request):
    miembro = Miembro.objects.all()
    context = {"miembro": miembro,}
    return render(request, 'member.html',context)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


def base(request):
    return render(request, 'core/base.html')