from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
import datetime
from django.utils import timezone


class Portada(models.Model):
    texto1 = models.TextField()
    texto2 = models.TextField()


    def __str__(self):
        return self.texto1


class Sobre_aneic(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    objetivos = models.TextField()



    def __str__(self):
        return self.titulo



class Preguntas_frecuentes(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        return self.titulo


class Miembro(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)
    cargo = models.CharField(max_length=300)
    link_instagram = models.CharField(max_length=300, default="#")
    link_twitter = models.CharField(max_length=300, default="#")
    link_whatsapp = models.CharField(max_length=300, default="#")
    link_email = models.CharField(max_length=300, default="#")


    def __str__(self):
        return self.nombre


class Categoria_1 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre


class Categoria_2 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre

class Categoria_3 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    categoria_1 = models.ForeignKey('Categoria_1', on_delete=models.CASCADE,null=True)
    categoria_2 = models.ForeignKey ('Categoria_2', on_delete=models.CASCADE, null=True)
    categoria_3 = models.ForeignKey('Categoria_3', on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def get_absolute_url(self):
        return reverse('single_blog', kwargs={'pk': self.pk})


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Convenio(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre


class Datos(models.Model):
    miembros = models.CharField(max_length=20)
    proyectos = models.CharField(max_length=20)
    conferencia = models.CharField(max_length=20)
    universidades = models.CharField(max_length=20)

    def __str__(self):
        return self.miembros



class Precio(models.Model):
    precio = models.CharField(max_length=20)
    tipo_suscripcion = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.precio

class Preciopro(models.Model):
    precio = models.CharField(max_length=20)
    tipo_suscripcion = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.precio

class Contacto(models.Model):
    direccion = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telefono_1 = models.CharField(max_length=300)
    telefono_2 = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return self.direccion



