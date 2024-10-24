"""aneicproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aneic import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('adminmk/', admin.site.urls),
    path('', views.raiz),
    path('inicio/', views.index),
    path('blog/', views.blog),
    path('blog/<int:pk>/', views.single_blog, name='single_blog'),
    path('suscripcion/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('base/', views.base),
    path('membresia/', views.membresia),
    path('comisiondirectiva/', views.comisiondirectiva),
    path('accounts/', include('django.contrib.auth.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
